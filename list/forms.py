from django.forms import ModelForm 
from list.models import Todo_list


class Todo_list_form(ModelForm):
    class Meta:
        model = Todo_list
        fields = ['title']

form = Todo_list() 