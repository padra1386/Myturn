from django.urls import path
from .views import homepage, appPage

urlpatterns = [
    path('', homepage, name="index"),
    path('app/', appPage, name="app")
]
