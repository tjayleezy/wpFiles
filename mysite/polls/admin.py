from django.contrib import admin

from .models import academic_dept, academic_class, file_manager
# Register your models here.

admin.site.register(academic_dept)
admin.site.register(academic_class)
admin.site.register(file_manager)
