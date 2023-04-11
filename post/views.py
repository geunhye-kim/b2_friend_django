from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
import os


def feed_view(request):
    if request.method == 'GET':
        post_list = Post.objects.all()
        return render(request, 'post/feed2.html',{post_list:post_list})


def post_create_view(request):
    pass


def post_view(request):
    pass


def post_update_view(request):
    pass


def post_delete_view(request):
    pass
