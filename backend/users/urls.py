from django.urls import path
from .views import RegisterView, LoginView, UserPublicView, UserPrivateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profiles/', UserPublicView.as_view()),
    path('profiles/my/', UserPrivateView.as_view()),
]