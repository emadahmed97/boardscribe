from django.contrib import admin

from .models import Classes,Notes

# Register your models here.
admin.site.register(Classes)


class NotesAdmin(admin.ModelAdmin):
        list_display = ('title','pub_date')
     	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Notes, NotesAdmin)
