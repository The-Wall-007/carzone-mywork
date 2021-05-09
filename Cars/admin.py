from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.car_photo .url))
    list_display = ['id','thumbnail','car_title','state','color','model','year','miles','doors','milage','is_featured']
    thumbnail.short_description = "Photo"
    search_fields = ['car_title','state','color','model']
    list_filter = ['car_title','color','model']
    list_editable = ['is_featured']

admin.site.register(Car,CarAdmin)
