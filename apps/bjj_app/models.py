from django.db import models
import re
from apps.login_app.models import User

# Create your models here.
class Move(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="moves")
    like = models.ManyToManyField(User, related_name="liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.name} {self.description} {self.creator} {self.user} {self.created_at} {self.updated_at}'

