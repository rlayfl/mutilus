from django.urls import path
from . import views

urlpatterns = [
    # For URLs with an experimentNumber
    path('<int:experimentNumber>/', views.experiment, name="experiment"),
    path('begin/<int:experimentNumber>/', views.begin, name='begin'),

    # Optional: Default URL to experiment with a default experiment number
    path('', views.experiment, {'experimentNumber': 1}, name='experiment_default'),
    path('begin/', views.begin, {'experimentNumber': 1}, name='begin_default'),
]
