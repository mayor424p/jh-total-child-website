from django.shortcuts import render, redirect
from django.conf import settings
from .forms import AdmissionForm
from reportlab.pdfgen import canvas
from io import BytesIO
import requests


def application_success(request):
    return render(request, 'admissions/application_success.html')


def apply_now(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)

        # ✅ reCAPTCHA check
        recaptcha_response = request.POST.get('g-recaptcha-response')

        if not recaptcha_response:
            form.add_error(None, "Please confirm you are not a robot.")
        else:
            data = {
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            response = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data=data
            )
            result = response.json()

            if not result.get('success'):
                form.add_error(None, "reCAPTCHA verification failed. Try again.")

        if form.is_valid():
            application = form.save()

            # 📄 Generate PDF
            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            p.setFont("Helvetica", 12)

            p.drawString(50, 800, f"Child: {application.surname} {application.other_names}")
            p.drawString(50, 780, f"Preferred Name: {application.preferred_name}")
            p.drawString(50, 760, f"DOB: {application.date_of_birth}")
            p.drawString(50, 740, f"Gender: {application.gender}")
            p.drawString(50, 720, f"Father: {application.father_name}, Phone: {application.father_phone}")
            p.drawString(50, 700, f"Mother: {application.mother_name}, Phone: {application.mother_phone}")
            p.drawString(50, 680, f"Address: {application.address}")
            p.drawString(50, 660, f"Medical: {application.other_medical_issues}")
            p.showPage()
            p.save()
            buffer.seek(0)

            return redirect('admissions:application_success')

    else:
        form = AdmissionForm()

    # ✅ PASS SITE KEY TO TEMPLATE (THIS WAS MISSING)
    return render(
        request,
        'admissions/apply_now.html',
        {
            'form': form,
            'current_page': 'apply_now',
            'RECAPTCHA_SITE_KEY': settings.RECAPTCHA_SITE_KEY,
           
        }
    )
