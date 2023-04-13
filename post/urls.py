from django.urls import path
from . import views


urlpatterns = [
    path('', views.feed_view, name='feed'),  # 피드 페이지
    path('feed/<str:region>/', views.feed_region_view,
         name='feed_region'),  # 지역별 피드 페이지
    path('post/create/', views.post_create_view, name='post_create'),  # 글쓰기 페이지
    path('post/<int:id>/', views.post_view, name='post'),  # 게시글 상세 페이지
    path('post/<int:id>/update/', views.post_update_view,name='post_update'),  # 게시글 수정하기
    path('post/<int:id>/delete/', views.post_delete_view, name='post_delete'),  # 게시글 삭제하기
    path('post/<int:id>/comment/', views.comment_create, name='comment'),  # 댓글 작성하기
    path('post/<int:id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),  # 댓글 삭제하기
]
