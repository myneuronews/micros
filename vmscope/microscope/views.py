from django.shortcuts import render
from django.views.generic import ListView
from .models import ParasiteImage

# Create your views here.
class ParasiteImageListView(ListView):
    model = ParasiteImage
    template_name = 'microscope/pr_image_list.html'
    context_object_name = 'images'
