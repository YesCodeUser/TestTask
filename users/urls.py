from django.urls import path
from .views import RegisterView, LoginView, LogoutView, MeView, UpdateView, DeleteUserView

urlpatterns = [
    path('reg/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('me/', MeView.as_view()),
    path('update/', UpdateView.as_view()),
    path('delete/', DeleteUserView.as_view())

]