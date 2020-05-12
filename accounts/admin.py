from django.contrib import admin
from .models import listOfProject, MilestoneObjects

# Register your models here.
class list(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(listOfProject,list)
admin.site.register(MilestoneObjects)
