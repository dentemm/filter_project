import datetime 

from django.db import models

# Create your models here.
class Filter(models.Model):

	product_code = models.CharField(max_length=255, unique=True)
	manufacturer = models.CharField(max_length=255)
	pore_size = models.CharField(max_length=32)
	is_stock_article = models.BooleanField(default=False)
	extra_info = models.TextField('Additional information', null=True, blank=True)

	class Meta:
		app_label = 'filter_app'
		verbose_name = 'filter'
		verbose_name_plural = 'filters'
		ordering = ['product_code',]

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
		ordering = ['name',]

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

	name = models.CharField(max_length=16, unique=True)
	slug = models.CharField(max_length=16, unique=False, blank=False, default='tja')
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
	'''
	Module for MES tool
	'''

	name = models.CharField(max_length=32, unique=False)
	main_tool = models.ForeignKey(Tool)
	current_filter = models.ForeignKey(Filter, related_name='+', blank=True, null=True)
	previous_filter = models.ForeignKey(Filter, related_name='+', blank=True, null=True) # No backwards relation!
	recommended_filter = models.ForeignKey(Filter, related_name='+', blank=True, null=True)
	chemistry = models.ManyToManyField(Chemistry, related_name='modules')
	swap_interval = models.IntegerField('Swap interval (# months)', null=True, default=24)
	extra_info = models.TextField(null=True, blank=True)
	number_of_filters = models.PositiveIntegerField('Number of filters', default=1)

	class Meta:
		app_label = 'filter_app'
		verbose_name = 'module'
		verbose_name_plural = 'modules'
		ordering = ['main_tool', 'name',]
		unique_together = ('name', 'main_tool', )

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.main_tool.name + '-' +self.name

	@property
	def last_swap(self):

		if self.swaps.count() > 0:

			#my_list = list(self.swaps.all())
			#return self.swaps[-1]

			last = self.swaps.all()[0]

			print "hier: " + str(last.date)

			return last

			#return my_list[-1]

		return None

	@property
	def time_to_next_swap(self):

		print 'time to next swap!!!'

		last_change = self.last_swap.date
		interval = self.swap_interval * 30

		next_change = last_change + datetime.timedelta(interval)


		time_to_next_swap = next_change - datetime.date.today()

		print "time_to_next_swap "
		print time_to_next_swap.days

		return time_to_next_swap.days

	

class FilterSwap(models.Model):

	#tool = models.ForeignKey(Tool, related_name='swaps')
	module = models.ForeignKey(Module, related_name='swaps')
	swapped_filter = models.ForeignKey(Filter, related_name='swaps')
	comment = models.TextField(null=True, blank=True)
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


		#elif not active_filter:

		print 'stel nieuwe filter in!'

		self.module.current_filter = self.swapped_filter

		self.module.save()

		super(FilterSwap, self).save(*args, **kwargs)
