from django.urls import path
from .views import SensorsView, SensorView, MeasurementView

urlpatterns = [
    path('sensor/', SensorsView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
]
