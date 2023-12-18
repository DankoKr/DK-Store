from django.urls import path
from . import views

# URL configuration
# API route + function
# Always add /
urlpatterns = [
    path('hello/', views.say_hello),
]