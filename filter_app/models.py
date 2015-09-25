from datetime import datetime

from django.db import models

# Create your models here.
class Filter(models.Model):

	product_code = models.CharField(max_length=255, unique=True)
	manufacturer = models.CharField(max_length=255)
	pore_size = models.CharField(max_length=32)

class Chemistry(models.Model):

	name = models.CharField(max_length=32)
	concentration = models.CharField(max_length=32)

class Tool(models.Model):

	name = models.CharField(max_length=32, unique=True)


class Module(models.Model):

	name = models.CharField(max_length=32)
	main_tool = models.ForeignKey(Tool)
	filters = models.ManyToManyField(Filter, related_name='modules')


class FilterHistory(models.Model):

	module = OneToOneField(Module)

	current_filter = models.ForeignKey(Filter)
	previous_filter = models.ForeignKey(Filter)

class FilterSwap(models.Model):

	module = models.ForeignKey(Module, related_name='swaps')
	swapped_filter = models.ForeignKey(Filter, related_name='swaps')
	comment = models.TextField()
	date = models.DateField('Date', default=datetime.date.today())

