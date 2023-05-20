from django.contrib import admin
#from django.forms import forms, Textarea
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.
from .models import *
# Register your models here.
class PythonSolutionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    formfield_overrides = { 
    models.TextField: {'widget': TinyMCE()} #optional, set Textarea attributes `attrs={'rows':2, 'cols':8}`
    }
admin.site.register(PythonSolution, PythonSolutionAdmin)