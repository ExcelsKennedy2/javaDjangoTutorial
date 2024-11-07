from django.urls import path
from kennedy_app import views

urlpatterns = [
    path('', views.home, name='My_index'),
    path('about/', views.about, name='my_about'),
    path('blog/', views.blog, name='my_blog'),
    path('contact/', views.contact, name='my_contact'),
    path('service/', views.services, name='my_services'),
    path('courses/', views.courses, name='my_courses'),
]