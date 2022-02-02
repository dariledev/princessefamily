from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class PostArticle(models.Model):
    titre = models.CharField(max_length=60)
    bio = models.TextField()
    picture = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titre




class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.username




class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    
    def __str__(self):
        return self.question



