from django.urls import path
from . import views

urlpatterns = [
    path('character_data/', views.character_data, name='character_data'),
    path('', views.main, name='main'),
    path('details/<str:fullname>/', views.details, name='details'),
    path('muse/', views.muse, name='muse'),
]