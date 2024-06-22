from django.contrib import admin
from .models import student

# Register your models here.
admin.site.register(student)
# students/admin.py


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV, XLS
#from .models import student
from .resources import StudentResource
from .formats import PDFFormat

#@admin.register(student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ('first_name', 'last_name', 'email', 'contact', 'date_of_birth', 'department', 'program', 'level')
    search_fields = ('first_name', 'last_name', 'email')

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            CSV,
            XLS,
            PDFFormat,
        )
        return [f() for f in formats]


