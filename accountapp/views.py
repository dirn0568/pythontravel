from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import Create_User_Form, Update_User_Form


class Create_User(CreateView):
    model = User
    form_class = Create_User_Form
    context_object_name = 'target_user'
    template_name = 'create_user.html'

    def get_success_url(self):
        return reverse('accountapp:login')

class Detail_User(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'detail_user.html'


class Update_User(UpdateView):
    model = User
    form_class = Update_User_Form
    context_object_name = 'target_user'
    template_name = 'update_user.html'

    def get_success_url(self):
        return reverse('accountapp:detail_user', kwargs={'pk': self.object.pk})


class Delete_User(DeleteView):
    model = User
    context_object_name = 'target_user'
    template_name = 'delete_user.html'
    success_url = reverse_lazy('mainapp:main')