from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='register'),
    path('login-signup/',views.LS,name='LS'),
    path('profile/',views.profile,name='profile'),
    path('update_profile/',views.updateProfile,name='update_profile')
] 
