from unicodedata import category
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePageView, CreatePostView

from .views import home, post, category

urlpatterns = [
    path("", home, name="root"),
    path("blog/<slug:url>/", post),
    path("category/<slug:url>/", category),
    path("home/", HomePageView, name="home"),
    path("comment/", CreatePostView.as_view(), name="add_post"),
]
