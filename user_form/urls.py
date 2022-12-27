from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from user_form import views

urlpatterns = [
    path('', views.create_user_form, name="deneme_url"),
    path('user_form/ajax/load-cities/', views.load_districts, name='ajax_load_cities'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
