from django.db import models

# Create your models here.


class Member(models.Model):
    member_name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
