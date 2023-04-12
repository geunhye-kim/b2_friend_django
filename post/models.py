from django.db import models
# from account.models import UserModel


class Post(models.Model):
    class Meta:
        db_table = "my_post"

    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    regions = (
        ('서울', '서울'),
        ('강원도', '강원도'),
        ('경기도', '경기도'),
        ('충청도', '충청도'),
        ('전라도', '전라도'),
        ('경상도', '경상도'),
        ('제주도', '제주도'),
    )
    region = models.CharField(choices=regions, max_length=3)
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
