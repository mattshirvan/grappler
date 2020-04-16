from django.db import models
from apps.login_app.models import User

# Create your models here.
class Message(models.Model):
    message = models.TextField()
    likes = models.ManyToManyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.message}'

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.comment} {self.user} {self.message}'

class Follow(models.Model):
    follow = models.ManyToManyField(User, related_name="follows")
    