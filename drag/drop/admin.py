from django.contrib import admin
from .models import DDMOdel

# Register your models here.

@admin.register((DDMOdel))
class DDMOdelAdmin(admin.ModelAdmin):
    list_display=['id','image']