from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListPlayer.as_view()),
    path('<int:pk>/', views.DetailPlayer.as_view()),
]