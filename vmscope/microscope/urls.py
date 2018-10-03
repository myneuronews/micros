from django.urls import path

from .views import ParasiteImageListView


urlpatterns = [
    path('images/', ParasiteImageListView.as_view(), name='image_list')
]