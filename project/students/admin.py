from django.contrib import admin
from .models import Students

class StudentsAdmin(admin.ModelAdmin):
    list_display=("std_name", "std_class", "image")
    search_fields=('std_id','std_name')
    list_filter=('std_class','std_name')
admin.site.register(Students,StudentsAdmin)
