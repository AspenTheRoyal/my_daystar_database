from django.urls import path
from . import views

urlpatterns = [
    path('avg_smogon/', views.avg_smogon_view, name='avg_smogon'),
    path('my_smogon_script', views.my_smogon_script, name='my_smogon_script'),
]