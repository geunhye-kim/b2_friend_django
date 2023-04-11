from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os


def feed_view(request):
    if request.method == 'GET':
        post_list = Post.objects.all()
        return render(request, 'post/feed2.html',{post_list:post_list})


def post_create_view(request):
    pass


def post_view(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'post/detail.html', {'post': post})


@login_required
def post_update_view(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'post/update.html', {'post': post})
    elif request.method == 'POST':
        post.title = request.POST.get('title','')
        post.post = request.POST.get('post','')
        post.region = request.POST.get('region','')
        if post.title == '' or post.post == '':
            return redirect('post_update', id=post.id)
        else:
            post.save()
            return redirect('feed')

@login_required
def post_delete_view(request, id):
    my_tweet = Post.objects.get(id=id)
    my_tweet.delete()
    return redirect('feed')