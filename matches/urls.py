from django.urls import path
from . import views

app_name = "matches"

urlpatterns = [
    path("", views.match_list, name="list"),
    path("new/", views.match_create, name="create"),
    path("<int:pk>/edit/", views.match_edit, name="edit"),
    path("<int:pk>/delete/", views.match_delete, name="delete"),
]
