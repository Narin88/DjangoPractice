from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

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