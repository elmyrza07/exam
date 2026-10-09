from django.urls import path

from posts.views import create_post, post_detail, post_list, toggle_complete

urlpatterns = [
    path("", post_list, name="post_list"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("post/create/", create_post, name="create_post"),
    path("post/<int:pk>/toggle/", toggle_complete, name="toggle_complete"),
]
