# myapp/urls.py

from django.urls import path
from . import views
# app_name = 'myapp' #
urlpatterns = [
    # Map the root URL of your app to the 'home' view
    path('', views.home, name='home'),     
    path('about/', views.about, name='about'),     
    path('blog/', views.blog, name='blog'),     
    path('login/', views.login_user, name='login'),     
    path('logout/', views.logout_user, name='logout'),     
    path('register/', views.register_user, name='register'),     
]