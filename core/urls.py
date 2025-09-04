from django.contrib import admin
from django.urls import path

from Notes.views import *
urlpatterns = [
    path("", view_page,name="view_page"),
    path("admin/", admin.site.urls),
    path("login/",login_page,name="login_page"),
    path("register/",register_page,name="register_page"),
    path("logout/",logout_page,name="logout_page"),
    path("home/",home_page,name="home_page"),
    path("add_notes/",add_notes,name="add_notes"),
    path("view_notes/",view_notes,name="view_notes"),
    path("edit_notes/<id>",edit_notes,name="edit_notes"),
    path("delete_notes/<id>",delete_notes,name="delete_notes"),
    path("view_page/",view_page,name="view_page")
]
