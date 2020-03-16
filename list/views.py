from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views import View
from .forms import Todo_list_form
from .models import Todo_list


class home(View):
    form_class = Todo_list_form
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
       form = self.form_class(request.POST)
       if form.is_valid():
           form.save()
           # <process form cleaned data>
        #    return HttpResponseRedirect('/success/')
           return HttpResponse("Updated ")
       return render(request, self.template_name, {'form': form})

class UpdatedList(ListView):
    queryset = Todo_list.objects.filter()
    template_name = 'home.html'
    context_object_name = 'AllList'
