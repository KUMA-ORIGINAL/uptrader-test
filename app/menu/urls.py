from django.urls import path

from menu import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('contact-1/', views.contact_view_1, name='contact-1'),
]
