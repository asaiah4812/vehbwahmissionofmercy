from django.contrib import admin
from core.models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']

@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ['title', 'slug', 'created']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Comment)
admin.site.register(About)
