from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scrape/', views.scrape_material_view, name='scrape'),
]
