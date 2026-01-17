from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.admin_signup, name='signup'),
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
]