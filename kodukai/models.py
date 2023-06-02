from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

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
    ITEM_CHOICES = (
        ('雑収','雑収'),
        ('雑費','雑費'),
        ('買い物','買い物'),
        ('飲食','飲食'),
        ('食費','食費'),
        ('入金','入金'),
        ('出金','出金'),
        ('交通費','交通費'),
        ('カード引落','カード引落'),
        ('振込','振込'),
        ('立替','立替'),
        ('繰越','繰越'),
    )
    KANJO1_CHOICES = (
        ('b', '銀行'),
        ('c', 'カード'),
        ('g', '現金'),
        ('d', '借金'),
        ('s', 'スイカ'),
        ('k', '費用'),
        ('t', '立替'),
        ('d', '引当金'),
        ('p', 'ペイペイ'),
        ('z', 'ダミー'),
    )
    KANJO2_CHOICES = (
        ('b', '銀行'),
        ('c', 'カード'),
        ('g', '現金'),
        ('d', '借金'),
        ('s', 'スイカ'),
        ('k', '収入'),
        ('t', '立替'),
        ('d', '引当金'),
        ('p', 'ペイペイ'),
        ('z', 'ダミー'),
    )
    use_date = models.DateField()
    item = models.CharField(
        verbose_name = "アイテム",
        max_length=20,
        choices=ITEM_CHOICES)
    debit = models.CharField(
        verbose_name = "勘定",
        max_length=1,
        choices=KANJO1_CHOICES)
    credit = models.CharField(
        verbose_name = "勘定",
        max_length=1,
        choices=KANJO2_CHOICES)
    amount = models.IntegerField(validators=[MinValueValidator(0),])

class ValidDate(models.Model):
    key = models.IntegerField(default=1)
    valid_date = models.DateField()

