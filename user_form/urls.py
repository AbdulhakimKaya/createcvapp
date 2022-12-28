from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from user_form import views

urlpatterns = [
    path('', views.index, name="home"),
    path('example/', views.example, name="example"),
    path('about/', views.about, name="about"),
    path('user-form/', views.create_user_form, name="user-form"),
    path('user_form/ajax/load-cities/', views.load_districts, name='ajax_load_cities'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
