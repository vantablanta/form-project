from django.db import models

# Create your models here.
class SubscriptionModel(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name