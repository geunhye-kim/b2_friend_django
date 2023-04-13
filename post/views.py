from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post,Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os


def feed_view(request):
    if request.method == 'GET':
        post_list = Post.objects.all()
        paginator = Paginator(post_list, per_page=8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'post/feed.html', {'page_obj': page_obj})


def feed_region_view(request, region):
    if request.method == 'GET':
        post_list = Post.objects.filter(region=region)
        paginator = Paginator(post_list, per_page=8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'post/feed.html', {'page_obj': page_obj})


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
    comments = Comment.objects.filter(post=post)
    if request.method == 'GET':
        return render(request, 'post/detail.html', {'post': post, 'comments':comments})


@login_required
def post_update_view(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        if request.user.id == post.user_id:
            post.title = request.POST.get('title', '')
            post.post = request.POST.get('post', '')
            post.region = request.POST.get('region', '')
            post.image = request.FILES.get('image') or post.image
            if post.title == '' or post.post == '':
                return redirect('post', id=post.id)
            else:
                post.save()
                return redirect('post', id=post.id)


@login_required
def post_delete_view(request, id):
    post = Post.objects.get(id=id)
    if request.user.id == post.user_id:
        post.delete()
    return redirect('feed')



@login_required
def comment_create(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        if comment == '':
            return redirect('post', post.id)
        else:
            Comment.objects.create(name= request.user.username, comment=comment, user=request.user, post=post)
            return redirect('post', post.id)


@login_required
def comment_delete(request, comment_id, id):
    comment = Comment.objects.get(id=comment_id)
    if request.user.id == comment.user_id:
        comment.delete()
    return redirect('post', comment.post.id)
    

@login_required
def comment_edit(request, id, comment_id):
    post = Post.objects.get(id=id)
    comment = Comment.objects.get(id=comment_id)
    if request.method == "POST":
        comment_data = request.POST.get('comment', '')
        if comment == '':
            return redirect('post', post.id)
        else:
            comment.comment = comment_data
            comment.save()
    return redirect('post', post.id)
    


