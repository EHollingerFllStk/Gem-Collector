from django.contrib import admin
# import your models here
from .models import Gem, Cleaning

# Register your models here
admin.site.register(Gem)
admin.site.register(Cleaning)


