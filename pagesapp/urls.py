from django.urls import path
from .views import HomePageWiew, AboutPageWiew

urlpatterns = [
    path('about/', AboutPageWiew.as_view(), name='about'),
    path('', HomePageWiew.as_view(), name='home'),
]