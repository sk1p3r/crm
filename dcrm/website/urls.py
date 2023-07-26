from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
   # Login page is appended on home, it can be created separate if you want
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]