from django.contrib import admin

from .models import Classes,Notes

# Register your models here.
admin.site.register(Classes)
admin.site.register(Notes)


class ClassesAdmin(admin.ModelAdmin):
        list_display = ('title')
