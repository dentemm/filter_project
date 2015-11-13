from django.forms import ModelForm, ModelChoiceField, BaseModelFormSet

from .models import FilterSwap, Module

class SwapForm(ModelForm):

	def __init__(self, tool, *args, **kwargs):

		super(SwapForm, self).__init__(*args, **kwargs)



		#tool = self.request.GET.get('tool', '')
		#print "here: " + str(tool)
		self.fields['module'] = ModelChoiceField(queryset=Module.objects.filter(main_tool__name__iexact=tool))




	class Meta:
		model = FilterSwap
		#fields = ['module', 'swapped_filter', 'comment', 'date', 'who']
		fields = '__all__'

'''
class TestForm(BaseModelFormSet):

	def __init__(self, tool, *args, **kwargs):

		super(TestForm, self).__init__(*args, **kwargs)

		self.queryset = SwapForm.objects.all()

	class Meta:

		model = FilterSwap
		fields = '__all__'
'''

