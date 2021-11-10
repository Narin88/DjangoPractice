from django.http.response import HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from accountapp.models import HelloWorld
from .forms import AccountUpdateForm

# Create your views here.
def index(request):

  if request.user.is_authenticated:
    if request.method == "POST":
      temp = request.POST.get('hello_world_input')

      new_hello_world = HelloWorld();
      new_hello_world.text = temp
      new_hello_world.save()

      return HttpResponseRedirect(reverse('accountapp:index'))
    else:
      hello_world_list = HelloWorld.objects.all()
      return render(request, 'accountapp/hello_world.html', context={ 'hello_world_list': hello_world_list })
  else:
    return HttpResponseRedirect(reverse('accountapp:login'))

class AcouuntCreateView(CreateView):
  model = User
  form_class = UserCreationForm
  success_url = reverse_lazy("accountapp:index")
  template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
  model = User
  context_object_name = 'target_user'
  template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
  model = User
  form_class = AccountUpdateForm
  context_object_name = 'target_user'
  success_url = reverse_lazy("accountapp:index")
  template_name = 'accountapp/update.html'

  def get(self, *args, **kwargs):
    # 로그인이 되어있는지 체크
    if self.request.user.is_authenticated and self.get_object() == self.request.user:
      return super().get(*args, **kwargs)
    else:
      return HttpResponseForbidden()

  def post(self, *args, **kwargs):
    # 로그인이 되어있는지 체크
    if self.request.user.is_authenticated and self.get_object() == self.request.user:
      return super().get(*args, **kwargs)
    else:
      return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
  model = User
  success_url = reverse_lazy('accountapp:login')
  context_object_name = 'target_user'
  template_name = 'accountapp/delete.html'

  def get(self, *args, **kwargs):
    # 로그인이 되어있는지 체크
    if self.request.user.is_authenticated and self.get_object() == self.request.user:
      return super().get(*args, **kwargs)
    else:
      return HttpResponseForbidden()

  def post(self, *args, **kwargs):
    # 로그인이 되어있는지 체크
    if self.request.user.is_authenticated and self.get_object() == self.request.user:
      return super().get(*args, **kwargs)
    else:
      return HttpResponseForbidden()