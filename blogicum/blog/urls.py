from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('',
         views.PostListView.as_view(),
         name='index'),
    path('posts/<int:post_id>/',
         views.PostDetailView.as_view(),
         name='post_detail'),
    path('category/<slug:category_slug>/',
         views.PostCategoryView.as_view(),
         name='category_posts'),
    path('posts/create/',
         views.PostCreateView.as_view(),
         name='create_post'),
    path('posts/<int:post_id>/edit/',
         views.PostUpdateView.as_view(),
         name='edit_post'),
    path('posts/<int:post_id>/delete/',
         views.PostDeleteView.as_view(),
         name='delete_post'),
    path('posts/<int:post_id>/comment/',
         views.CommentCreateView.as_view(),
         name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:pk>',
         views.EditCommentView.as_view(),
         name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:pk>',
         views.DeleteCommentView.as_view(),
         name='delete_comment'),
    path('profile/<slug:username>/',
         views.ProfileView.as_view(),
         name='profile'),
    path('profile/<slug:username>/edit/',
         views.ProfileEditView.as_view(),
         name='edit_profile'),
]