from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=32, unique=True)
    owner = models.ForeignKey(User, related_name="players", on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
