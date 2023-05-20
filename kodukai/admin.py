from django.contrib import admin
from .models import Item, Kanjo, Treasurer, ValidDate

# Register your models here.

admin.site.register(Item)
admin.site.register(Kanjo)
admin.site.register(Treasurer)
admin.site.register(ValidDate)
