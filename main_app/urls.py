from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gems/', views.gems_index, name='index'),
    path('gems/<int:gem_id>/', views.gem_detail, name='detail'),
]