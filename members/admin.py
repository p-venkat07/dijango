from django.contrib import admin
from .models import Member,year
# Register your models here.
class GLUGview(admin.ModelAdmin):

    list_display  = ['name','designation']
    search_fields = ['name']

admin.site.register(Member,GLUGview)
admin.site.register(year)
