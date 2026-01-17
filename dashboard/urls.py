from django.urls import path
from . import views 

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='home'),

    path('applications/<int:pk>/', views.application_detail, name='application_detail'),

    path('applications/approve/<int:pk>/', views.approve_application, name='approve'),
    path('applications/reject/<int:pk>/', views.reject_application, name='reject'),
    path('applications/delete/<int:pk>/', views.delete_application, name='delete_application'),

    path('gallery/add/', views.add_image, name='add_image'),
    path('gallery/delete/<int:pk>/', views.delete_image, name='delete_image'),
]