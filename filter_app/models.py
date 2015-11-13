import datetime 

from django.db import models

# Create your models here.
class Filter(models.Model):

	product_code = models.CharField(max_length=255, unique=True)
	manufacturer = models.CharField(max_length=255)
	pore_size = models.CharField(max_length=32)

	class Meta:
		app_label = 'filter_app'
		verbose_name = 'filter'
		verbose_name_plural = 'filters'

	def __unicode__(self):
		return self.product_code

	def __str__(self):
		return self.product_code

class Chemistry(models.Model):

	name = models.CharField(max_length=32)
	concentration = models.CharField(max_length=32)

	class Meta:
		app_label = 'filter_app'
		verbose_name = 'chemistry'
		verbose_name_plural = 'chemicals'

	def __unicode__(self):
		return str(self.name) + ' ' + str(self.concentration)

	def __str__(self):
		return str(self.name) + ' ' + str(self.concentration)

	def description(self):
		return str(self.name) + ' ' + str(self.concentration)

class Tool(models.Model):

	CR_CHOICES = (
	    ('FAB1', 'FAB1'),
	    ('FAB2', 'FAB2'),
	)

	name = models.CharField(max_length=8, unique=True)
	cleanroom = models.CharField(max_length=16, choices=CR_CHOICES, default='FAB1', null=True)

	class Meta:
		app_label = 'filter_app'
		verbose_name = 'tool'
		verbose_name_plural = 'tools'
		ordering = ['cleanroom', 'name', ]

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Module(models.Model):

	name = models.CharField(max_length=32, unique=True)
	main_tool = models.ForeignKey(Tool)
	current_filter = models.ForeignKey(Filter, related_name='modules')
	previous_filter = models.ForeignKey(Filter, related_name='+', null=True) # No backwards relation!
	chemistry = models.ManyToManyField(Chemistry, related_name='modules')

	class Meta:
		app_label = 'filter_app'
		verbose_name = 'module'
		verbose_name_plural = 'modules'

	def __unicode__(self):
		return self.main_tool.name + '-' +self.name

	def __str__(self):
		return self.main_tool.name + '-' +self.name

class FilterSwap(models.Model):

	#tool = models.ForeignKey(Tool, related_name='swaps')
	module = models.ForeignKey(Module, related_name='swaps')
	swapped_filter = models.ForeignKey(Filter, related_name='swaps')
	comment = models.TextField()
	date = models.DateField('Date', default=datetime.date.today)
	who = models.CharField(max_length=32, null=True)

	class Meta:
		app_label = 'filter_app'
		verbose_name = 'filter swap'
		verbose_name_plural = 'filter swaps'
		ordering = ['-date']

	def __unicode__(self):
		return str(self.module) + ': filter changed on ' + str(self.date)

	def __str__(self):
		return str(self.module) + ': filter changed on ' + str(self.date)

	def save(self, *args, **kwargs):

		active_filter = self.module.current_filter

		if active_filter and self.swapped_filter != active_filter:

			self.module.previous_filter = active_filter

			print 'filter swapped!'
			print self.module.previous_filter

		super(FilterSwap, self).save(*args, **kwargs)
