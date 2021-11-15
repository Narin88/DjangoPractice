from django.db import models

# Create your models here.
class Project(models.Model):
  image = models.ImageField(upload_to='project/', null=False)
  title = models.CharField(max_length=200, null=False)
  # 프로젝트 설명
  description = models.CharField(max_length=200, null=True)

  # 만들어진 날짜
  created_at = models.DateField(auto_now_add=True)