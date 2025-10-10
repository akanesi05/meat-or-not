from django.urls import path
from . import views

urlpatterns = [
    path('', views.top_view, name='top'),
    path('input/', views.input_view, name='input'),
    path('result/', views.result_view, name='result'),
    
]
