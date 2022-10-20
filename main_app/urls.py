from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gems/', views.gems_index, name='index'),
    path('gems/<int:gem_id>/', views.gem_detail, name='detail'),
    path('gems/create/', views.GemCreate.as_view(), name='gems_create'),
    path('gems/<int:pk>/update/', views.GemUpdate.as_view(), name='gems_update'),
    path('gems/<int:pk>/delete/', views.GemDelete.as_view(), name='gems_delete'),
    path('gems/<int:gem_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('jewelry/', views.JewelryList.as_view(), name='jewelry_index'),
    path('jewelry/<int:pk>/', views.JewelryDetail.as_view(), name='jewelry_detail'),
    path('jewelry/create/', views.JewelryCreate.as_view(), name='jewelry_create'),
    path('jewelry/<int:pk>/update/', views.JewelryUpdate.as_view(), name='jewelry_update'),
    path('jewelry/<int:pk>/delete/', views.JewelryDelete.as_view(), name='jewelry_delete'),
    path('gems/<int:gem_id>/assoc_jewelry/<int:jewelry_id>/', views.assoc_jewelry, name='assoc_jewelry'),
]

