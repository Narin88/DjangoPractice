from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from accountapp.models import HelloWorld

# Create your views here.
def index(request):

  if request.method == "POST":
    temp = request.POST.get('hello_world_input')

    new_hello_world = HelloWorld();
    new_hello_world.text = temp
    new_hello_world.save()

    hello_world_list = HelloWorld.objects.all()
    return HttpResponseRedirect(reverse('accountapp:index'))
  else:
    hello_world_list = HelloWorld.objects.all()
    return render(request, 'accountapp/hello_world.html', context={ 'hello_world_list': hello_world_list })

class AcouuntCreateView(CreateView):
  model = User
  form_class = UserCreationForm
  success_url = reverse_lazy("accountapp:index")
  template_name = 'accountapp/create.html'