from django.urls import path
from . import views

app_name = "solution"

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:id>/", views.solution, name = "solution"),
]