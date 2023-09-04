from django.urls import path

from playground import views

urlpatterns = [
    path('welcome/', views.welcome)
]
