from django.contrib import admin
from .models import Parasite, ParasiteImage, ParasiteStage

# Register your models here.
admin.site.register(ParasiteImage)
admin.site.register(Parasite)
admin.site.register(ParasiteStage)
