from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)  # VARCHAR
    description = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateField()


    def __str__(self):
        return f"Name Book: {self.title} About: {self.description}"


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=250, null=True, blank=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         db_table = "posts"  # Название таблицы

class UserProfile(models.Model):
    nickname = models.CharField(max_length=70, unique=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    age = models.PositiveSmallIntegerField()
    followers_count = models.PositiveBigIntegerField()
    posts_count = models.PositiveIntegerField()
    comments_count = models.PositiveIntegerField()
    engagement_rate = models.FloatField()
#
#     def __str__(self):
#         return self.nickname
#
#     class Meta:
#         db_table = "user_profile"  # Название таблицы








# from enum import StrEnum

# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin, UserManager
# from django.core.validators import MinValueValidator, MaxValueValidator

# from django.utils.translation.trans_null import gettext_lazy as _
# from django.utils import timezone