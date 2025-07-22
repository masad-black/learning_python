from django.urls import path

from . import views

print("----- Start -----")

urlpatterns = [
    path(
        "/",
        views.index,
        name="index",
    )
]
