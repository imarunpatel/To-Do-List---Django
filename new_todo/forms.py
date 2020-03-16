from .models import *
from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(
		attrs = {
			'class': 'form-control',
			'placeholder': 'Write your task here..'
		}
		))
	class Meta:
		model = Task 
		fields = '__all__'
