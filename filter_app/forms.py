from django.forms import ModelForm, ModelChoiceField, BaseModelFormSet
from django.forms.models import inlineformset_factory

from .models import FilterSwap, Module, Filter

class SwapForm(ModelForm):

	def __init__(self, tool, *args, **kwargs):

		super(SwapForm, self).__init__(*args, **kwargs)

		
		if tool != '':
			print 'tis ni gelijk'
			self.fields['module'] = ModelChoiceField(queryset=Module.objects.filter(main_tool__name__iexact=tool), to_field_name='name')

		else:
			print 'tis gelijk'
			self.fields['module'] = ModelChoiceField(queryset=Module.objects.all(), to_field_name='name')

		self.fields['swapped_filter'] = ModelChoiceField(queryset=Filter.objects.all(), to_field_name='product_code')


	class Meta:
		model = FilterSwap
		#fields = ['module', 'swapped_filter', 'comment', 'date', 'who']
		fields = '__all__'

class FilterForm(ModelForm):

	class Meta:
		model = Filter
		fields = '__all__'


