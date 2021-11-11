from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    # OneToOneField: tclass Profile과 user객체를 하나씩 연결해주는것
    # on_delete=models.CASCADE: 이 연결되어있는 user객체가 delete될때 그 와 연결되어있는 profile객체가 어떻게 될것인지 지정
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
