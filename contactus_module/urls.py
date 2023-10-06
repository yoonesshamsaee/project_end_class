from django.urls import path

from . import views
app_name = 'contactus_module'
urlpatterns = [
    path('',views.contactus_func,name='contactus_module'),
    path('register/',views.user_register,name='user-register'),
    path('login',views.user_login,name='user-login'),
    path('logout',views.user_logout,name='logout'),
]