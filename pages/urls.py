from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('references/', views.references_view, name='references'),
    path('admin-preview/', views.admin_preview_view, name='admin_preview'),
]
