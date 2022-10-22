from django.urls import path
from .views import RegisterView, LoginView, ProfilePublicView, ProfilePrivateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profiles/', ProfilePublicView.as_view()),
    path('profiles/my/', ProfilePrivateView.as_view()),
]