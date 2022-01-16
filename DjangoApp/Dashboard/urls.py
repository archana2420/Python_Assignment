from django.urls import path
from .views import RegisterationPage,LoginPage,LogoutPage,DashboardPage

urlpatterns = [
    path('',RegisterationPage,name='register'),
    path('login/',LoginPage,name='login'),
    path('logout/',LogoutPage,name='logout'),
    path('dashboard/',DashboardPage,name='dashboard')

]