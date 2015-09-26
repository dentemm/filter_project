from django.forms import ModelForm

from .models import FilterSwap

class SwapForm(ModelForm):

	class Meta:
		model = FilterSwap
		#fields = ['module', 'swapped_filter', 'comment', 'date', 'who']
		fields = '__all__'

