from django.urls import path
from . import views

app_name = 'analyzer'

urlpatterns = [
    path('', views.web_analyze, name='web_form'),
    path('analyze/', views.web_analyze, name='web_analyze'),
    path('api/analyze/', views.api_analyze, name='api_analyze'),
]
