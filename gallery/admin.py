from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'show_on_homepage', 'created_at')
    list_filter = ('category', 'show_on_homepage')
    search_fields = ('title',)
    

# Register your models here.

