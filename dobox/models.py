from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.CharField(max_length = 100)
    amount = models.FloatField(default=0.0)
    type = models.CharField(max_length=100, default="Spent")

    def __str__(self):
        return self.transaction + "; " + str(self.amount) + "; " + self.type