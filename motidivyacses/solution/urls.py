from django.urls import path
from . import views

app_name = "solution"

urlpatterns = [
    path("<int:id>/", views.index, name = "index"),
]