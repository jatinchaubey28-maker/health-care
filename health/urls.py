from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('about-us/', views.about,name="about"),
    path('contact-us/', views.contact,name="contact-us"),
    path('service/', views.service,name="service"),
    path('all-doctor/<int:id>', views.all_doctors,name="all_doctor"),
    path('doctor-single/<int:id>', views.single_doctor_details,name="doctor_single"),
    path('appointment', views.appointment_book,name="appointment"),
    path('get-doctor-department-name-ajax/', views.get_doctors, name='get-doctor-department-name-ajax'),
    path('confirmation', views.confirmation, name="confirmation"),
    path('subscribe/', views.subscribe_newsletter, name='subscribe'),
    path('appointment/<int:id>', views.appointment_book, name="appointment_doctor"),
]
