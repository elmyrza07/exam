from django.contrib import admin
from django.urls import include, path
from posts.views import post_detail, post_list, post_create, post_delete, post_edit, my_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/create/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('my-posts/', my_posts, name='my_posts'),
    path('accounts/', include('django.contrib.auth.urls')),
]