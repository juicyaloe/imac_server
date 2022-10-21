from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trade(models.Model):
    description = models.TextField(default="")
    seller = models.ForeignKey(User, related_name="seller", on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name="buyer", on_delete=models.CASCADE)

    def __str__(self):
        return self.seller.username + "님과 " + self.buyer.username + "님의 거래"
