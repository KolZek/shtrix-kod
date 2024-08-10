from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("posts.urls", namespace="index")),
    path("admin-skod/", admin.site.urls),
]
