from datetime import datetime

from django.forms import ModelForm, ModelChoiceField, BaseModelFormSet
from django.forms.models import inlineformset_factory

from .models import FilterSwap, Module, Filter

class SwapForm(ModelForm):

	def __init__(self, tool, *args, **kwargs):

		super(SwapForm, self).__init__(*args, **kwargs)

		if tool != '':
			self.fields['module'] = ModelChoiceField(queryset=Module.objects.filter(main_tool__name__iexact=tool), to_field_name='name')

		else:
			self.fields['module'] = ModelChoiceField(queryset=Module.objects.all(), to_field_name='name')

		self.fields['swapped_filter'] = ModelChoiceField(queryset=Filter.objects.all(), to_field_name='product_code')
	

	def clean(self):

		print("self: %s" % self)

		cleaned_data = super(SwapForm, self).clean()

		date = cleaned_data['date']

		print('jaar: %s' % date.year)

		if date.year == 4444:

			print('------- 4444')

			cleaned_data['date'] = datetime.today()


		return cleaned_data


	class Meta:
		model = FilterSwap
		#fields = ['module', 'swapped_filter', 'comment', 'date', 'who']
		fields = '__all__'

class FilterForm(ModelForm):

	class Meta:
		model = Filter
		fields = '__all__'


