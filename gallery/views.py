from django.shortcuts import render
from .models import GalleryImage

def gallery_page(request):
    images = GalleryImage.objects.all().order_by('-created_at')

    category_filter = request.GET.get('category', 'all')

    if category_filter != 'all':
        images = images.filter(category=category_filter)

    total_images = GalleryImage.CATEGORY_CHOICES

    context = {
        'images': images,
        'total_images': total_images,
        'current_category': category_filter,
        'categories': GalleryImage.CATEGORY_CHOICES,
        'current_page': 'gallery'
    }
    return render(request, 'gallery/gallery.html', context)
# Create your views here.
