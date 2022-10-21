from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trade(models.Model):
    description = models.TextField(default="", blank=True, null=True)
    seller = models.ForeignKey(User, related_name="selling", on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name="buying", on_delete=models.CASCADE)

    targetPlayer = models.OneToOneField("players.Player", related_name="trading", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.seller.username + "님과 " + self.buyer.username + "님의 거래"
