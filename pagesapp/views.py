from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageWiew(TemplateView):
    template_name = 'home.html'

class AboutPageWiew(TemplateView):
    template_name = 'about.html'
