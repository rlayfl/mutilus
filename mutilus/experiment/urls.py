from django.urls import path
from . import views

urlpatterns = [
    # For URLs with an alphanumeric experiment identifier
    path('<str:experimentNumber>/', views.experiment, name="experiment"),
    path('begin/<str:experimentNumber>/', views.begin, name='begin'),

    # Optional: Default URL to experiment with a default experiment identifier
    path('', views.experiment, {'experimentNumber': 'default_experiment'}, name='experiment_default'),
    path('begin/', views.begin, {'experimentNumber': 'default_experiment'}, name='begin_default')    
]
