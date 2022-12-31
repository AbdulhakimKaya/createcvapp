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
    path('design-page/', views.design_page, name="design-page"),
    path('pdf/<int:id>', views.users_render_pdf_view, name='user_pdf_view'),
    path('user_form/ajax/load-cities/', views.load_districts, name='ajax_load_cities'),
    path('user_form/ajax/load-lang-levels/', views.load_lang_levels, name='ajax_load_lang_levels'),
    path('user_form/ajax/load-ability-levels/', views.load_ability_levels, name='ajax_load_ability_levels'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
