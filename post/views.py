from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os


def feed_view(request):
    if request.method == 'GET':
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'post/feed.html', {'post_list': post_list, 'page_obj': page_obj})


def feed_region_view(request, region):
    if request.method == 'GET':
        post_list = Post.objects.filter(region=region)
        paginator = Paginator(post_list, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'post/feed.html', {'post_list': post_list, 'page_obj': page_obj})


def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'post/create.html')

    elif request.method == 'POST':
        title = request.POST.get('title', '')
        region = request.POST.get('region', '')
        image = request.FILES.get('image')
        content = request.POST.get('post', '')

        if title == '' or region == '지역 선택!':
            return render(request, 'post/create.html', {'error': '제목과 지역은 필수입니다!'})
        else:
            post = Post.objects.create(
                title=title, region=region, image=image, post=content, user=request.user)
            return redirect('post', post.id)
            # return redirect('feed')


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
        post.title = request.POST.get('title', '')
        post.post = request.POST.get('post', '')
        post.region = request.POST.get('region', '')
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
