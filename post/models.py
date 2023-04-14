from django.db import models
from user.models import UserModel


class Post(models.Model):
    class Meta:
        db_table = "my_post"

    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="mypost")
    title = models.CharField(max_length=256)
    regions = (
        ('서울', '서울'),
        ('강원도', '강원도'),
        ('경기도', '경기도'),
        ('충청도', '충청도'),
        ('전라도', '전라도'),
        ('경상도', '경상도'),
        ('제주도', '제주도'),
        ('평양', '평양'),
    )
    region = models.CharField(choices=regions, max_length=3)
    image = models.ImageField(upload_to='', null=True, blank=True)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    class Meta:
        db_table = "my_comment"

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
