from django.urls import path
from .views import gallery_page

app_name = 'gallery'

urlpatterns = [
    path('', gallery_page, name='gallery'),
]