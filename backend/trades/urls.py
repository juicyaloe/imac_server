from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListTrade.as_view()),
    path('<int:pk>/', views.DetailTrade.as_view()),
]