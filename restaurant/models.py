from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
  capacity = models.PositiveSmallIntegerField(default=3)
  is_occupied = models.BooleanField(default=False)


class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
	name = models.CharField(max_length=25)
	bill = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	table = models.ForeignKey(Table, on_delete=models.SET_NULL, related_name='table', default=None, null=True, blank=True)

	order = {}

	def __str__(self):
		return self.name

	def update_bill(self):
		total = 0
		for food in self.order:
			total += food.price * self.order[food]
		self.bill = total
		self.save()

	def add_item(self, item, qty):
		self.order[item] = qty
		self.update_bill()

	def reset(self):
		self.bill = 0
		self.order = {}
		self.save()


class Categories(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Item(models.Model):
	name = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	category = models.ManyToManyField(
		Categories,
		related_name="items",
		related_query_name="item"
	)
	descriptuon = models.TextField(max_length=50)

	def __str__(self):
		return self.name

