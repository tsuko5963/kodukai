from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class Item(models.Model):
    item = models.CharField(max_length=20)

    def __str__(self):
        return self.item

class Kanjo(models.Model):
    kanjo = models.CharField(max_length=1)
    name = models.CharField(max_length=10)

    def __srt__(self):
        return self.name

class Treasurer(models.Model):
    use_date = models.DateTimeField()
    item = models.CharField(max_length=20)
    debit = models.CharField(max_length=1)
    credit = models.CharField(max_length=1)
    amount = models.IntegerField()

class ValidDate(models.Model):
    valid_date = models.DateTimeField()
