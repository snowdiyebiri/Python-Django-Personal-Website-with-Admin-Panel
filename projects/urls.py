from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('search/', views.search_view, name='search'),
    path('activate-theme/<int:theme_id>/', views.activate_theme, name='activate_theme'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
]
