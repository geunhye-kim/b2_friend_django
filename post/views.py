from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse


def feed_view(request):
    return HttpResponse("안녕하세요")


def post_create_view(request):
    pass


def post_view(request):
    pass


def post_update_view(request):
    pass


def post_delete_view(request):
    pass
