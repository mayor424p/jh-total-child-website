from django.shortcuts import render
from gallery.models import GalleryImage

def home(request):
    homepage_images = GalleryImage.objects.filter(show_on_homepage=True).order_by('-created_at')[:4]

    return render(request, 'pages/home.html', {
        'homepage_images': homepage_images,
         'current_page': 'home',
    })


# Create your views here.
    