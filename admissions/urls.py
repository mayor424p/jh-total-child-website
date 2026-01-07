from django.urls import path
from .views import apply_now, application_success

app_name = 'admissions' 

urlpatterns = [
    path('', apply_now, name='apply_now'),
    path('success/', application_success, name='application_success'),
]
