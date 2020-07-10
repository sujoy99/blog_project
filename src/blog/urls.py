from django.urls import path
from .views import(
    blog_post_list_view,
    blog_post_detail_view,
    blog_post_update_view,
    blog_post_delete_view
)

app_name = "blog_post"
urlpatterns = [

    path('', blog_post_list_view, name='blog-list'),
    path('<str:slug>/', blog_post_detail_view, name='blog-detail'),
    path('<str:slug>/edit/', blog_post_update_view, name='blog-edit'),
    path('<str:slug>/delete/', blog_post_delete_view, name='blog-delete'),
]