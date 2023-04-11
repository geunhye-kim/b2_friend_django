from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feed'),  # 피드 페이지
    path('post/create/', views.post_create_view, name='post_create'),  # 글쓰기 페이지
    path('post/<int:pk>/', views.post_view, name='post'),  # 게시글 상세 페이지
    path('post/<int:pk>/update/', views.post_update_view,
         name='post_update'),  # 게시글 수정하기
    path('post/<int:pk>/delete/', views.post_delete_view,
         name='post_delete'),  # 게시글 삭제하기
]