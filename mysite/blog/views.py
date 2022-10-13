from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from django.urls import reverse_lazy

from .forms import CommentForm
from django.views.generic import ListView, CreateView

# Create your views here.
def home(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    data = {"posts": posts, "cats": cats}
    return render(request, "home.html", data)


def post(request, url):
    posts = Post.objects.get(url=url)
    cats = Category.objects.all()

    data = {"posts": posts, "cats": cats}

    return render(request, "posts.html", data)


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {"cat": cat, "posts": posts})


def post_detail(request):
    form = CommentForm()
    cats = Category.objects.all()
    return render(request, "posts.html", {"form": form})


def HomePageView(request):
    data = Comment.objects.all()
    return render(request, "test/comment2.html", {"data": data})


class CreatePostView(CreateView):
    model = Post
    form_class = CommentForm
    template_name = "comment.html"
    success_url = reverse_lazy("home")
