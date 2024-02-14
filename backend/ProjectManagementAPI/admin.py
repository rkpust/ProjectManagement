from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Manager)
# admin.site.register(Project)
admin.register(Manager, Project)(admin.ModelAdmin) # to register multiple model
