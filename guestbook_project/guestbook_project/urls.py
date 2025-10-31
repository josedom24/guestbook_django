from django.contrib import admin
from django.urls import path
from guestbook import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("add/", views.add, name="add"),
]
