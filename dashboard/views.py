from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test\

from admissions.models import AdmissionApplication
from gallery.models import GalleryImage
from .forms import GalleryImageForm
from django.core.mail import send_mail
from django.conf import settings

def staff_required(user):
    return user.is_staff


@login_required
@user_passes_test(staff_required)
def dashboard(request):
    tab = request.GET.get('tab', 'applications')
    applications = AdmissionApplication.objects.order_by('-submitted_at')
    images = GalleryImage.objects.order_by('-created_at')

    context = {
        'tab': tab,
        'applications': applications,
        'images': images,

        'pending_count': applications.filter(status='pending').count(),
        'approved_count': applications.filter(status='approved').count(),
        'rejected_count': applications.filter(status='rejected').count(),
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
@user_passes_test(staff_required)
def approve_application(request, pk):
    app = get_object_or_404(AdmissionApplication, pk=pk)
    app.status = 'approved'
    app.save()

    if app.father_email:
        subject = "Admission Approved!"
        message = f"Dear {app.surname} {app.other_names},\n\n" \
                  f"Congratulations! Your admission application has been approved.\n\n" \
                  f"Best regards,\nJH Total Child Academy"
        
        recipient_list = [app.father_email]

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False)
    return redirect('/dashboard/?tab=applications')


@login_required
@user_passes_test(staff_required)
def reject_application(request, pk):
    app = get_object_or_404(AdmissionApplication, pk=pk)
    app.status = 'rejected'
    app.save()
    return redirect('/dashboard/?tab=applications')


@login_required
@user_passes_test(staff_required)
def delete_application(request, pk):
    app = get_object_or_404(AdmissionApplication, pk=pk)
    app.delete()
    return redirect('/dashboard/?tab=applications')

@login_required
@user_passes_test(staff_required)
def add_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/?tab=gallery')
    else:
        form = GalleryImageForm()

    return render(request, 'dashboard/add_image.html', {'form': form})

@login_required
@user_passes_test(staff_required)
def delete_image(request, pk):
    img = get_object_or_404(GalleryImage, pk=pk)
    img.delete()
    return redirect('/dashboard/?tab=gallery')



@login_required
@user_passes_test(staff_required)
def application_detail(request, pk):
    application = get_object_or_404(AdmissionApplication, pk=pk)

    return render(
        request,
        'dashboard/application_detail.html',
        {
            'application': application
        }
    )
