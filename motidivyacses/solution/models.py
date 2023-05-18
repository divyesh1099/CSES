from django.db import models

# Create your models here.
class PythonSolution(models.Model):
    title = models.CharField(max_length=100)
    task = models.TextField(null = True, blank = True)
    code = models.TextField(null = True, blank = True)
    accepted = models.BooleanField(default=False)
    explanation = models.TextField(null = True, blank = True)
    time_complexity = models.CharField(null=True, blank=True, max_length=100)
    aod = models.TextField(blank = True, null = True)
    edited = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title