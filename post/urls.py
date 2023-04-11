from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.feed_view, name='feed'),  # 피드 페이지
    path('post/create/', views.post_create_view, name='post_create'),  # 글쓰기 페이지
    path('post/<int:id>/', views.post_view, name='post'),  # 게시글 상세 페이지
    path('post/<int:id>/update/', views.post_update_view, name='post_update'),  # 게시글 수정하기
    path('post/<int:id>/delete/', views.post_delete_view, name='post_delete'),  # 게시글 삭제하기
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
