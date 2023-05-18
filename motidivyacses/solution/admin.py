from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class PythonSolutionAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(PythonSolution, PythonSolutionAdmin)