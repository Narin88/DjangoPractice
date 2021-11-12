from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
  # related_name: User객체에서 Article에 접근할때 쓰는 이름 지정
  writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)

  title = models.CharField(max_length=200, null=True)
  image = models.ImageField(upload_to='article/', null=False)
  content = models.TextField(null=True)

  created_at = models.DateField(auto_now_add=True, null=True)