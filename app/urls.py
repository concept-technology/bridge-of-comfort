from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about-us'),
    path('donate', views.donor_create_view, name='donate'),
]
