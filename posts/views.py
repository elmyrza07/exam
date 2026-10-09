from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from posts.forms import PostForm
from posts.models import Post


def post_list(request: HttpRequest):
    posts = Post.objects.all()
    
    if search := request.GET.get("search"):
        posts = posts.filter(description__icontains=search)
        
    return render(request, "posts/list.html", context={"posts": posts})


def post_detail(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detail.html", context={"post": post})


def create_post(request: HttpRequest):
    if request.method.lower() == "post":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()

    return render(request, "posts/create.html", {"form": form})


def toggle_complete(request: HttpRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.is_completed = not post.is_completed
        post.save()
    return redirect("post_list")