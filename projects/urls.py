from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('search/', views.search_view, name='search'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]
