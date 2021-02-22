from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),
    path('result', views.result)
]