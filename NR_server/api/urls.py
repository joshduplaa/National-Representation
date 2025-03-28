from django.urls import path
from . import views
from .views import get_user

urlpatterns = [
    path("", views.index, name="index"),
    path('users/', get_user, name='get_user')
]