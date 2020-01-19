from django.contrib import admin

from .models import Categories, Customer, Item, Table

# Register your models here.
admin.site.register(Categories)
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Table)