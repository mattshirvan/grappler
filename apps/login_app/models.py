from django.db import models
import re


EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters"
        if len(postData['username']) < 2:
            errors['username'] = "Username must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email"
        if len(postData['password']) < 8 or len(postData['confirm']) < 8:
            errors['password'] = "Password must be at least 8 charachters"
        if postData['confirm'] != postData['password']:
            errors['confirm'] = "Passwords must match"
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=60)
    hash = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f'{self.name} {self.username} {self.email} {self.hash}'
