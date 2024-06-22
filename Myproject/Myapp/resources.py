# students/resources.py
from import_export import resources
from .models import student

class StudentResource(resources.ModelResource):
    class Meta:
        model = student
        fields = ('id', 'first_name', 'last_name', 'email', 'contact', 'date_of_birth', 'department', 'program', 'level')
        export_order = fields
