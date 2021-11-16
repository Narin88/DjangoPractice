from django.http.response import HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin
from accountapp.decorators import account_ownership_required

from accountapp.models import HelloWorld
from articleapp.models import Article
from .forms import AccountUpdateForm

has_ownership = [account_ownership_required, login_required]

# Create your views here.
# 로그인을 했는지 안했는지 확인하는 어노테이션 장고에서 기본제공


@login_required
def index(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:index'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AcouuntCreateView(CreateView):
    # 장고에서 기본적으로 제공해주는 model
    model = User
    # 장고에서 만들어주는 기본적인 폼
    form_class = UserCreationForm
    # 성공시 redirect할 url
    # 함수view에선 reverse를 쓰지만 클래스 view에선 reverse_lazy를 써야한다.
    success_url = reverse_lazy("accountapp:index")
    # 보여줄 템플릿 위치
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

# 일반 def에서 사용하는 데코레이터를 메소드에서 사용 할 수 있도록 변환해주는 데코레이터
@method_decorator(has_ownership, 'get')  # 사용할 메소드, 적용할 method이름
@method_decorator(has_ownership, 'post')  # 사용할 메소드, 적용할 method이름
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy("accountapp:index")
    template_name = 'accountapp/update.html'

# 배열로 넣을시 배열에 있는 메소드들을 모두 확인한다
@method_decorator(has_ownership, 'get')  # 사용할 메소드, 적용할 method이름
@method_decorator(has_ownership, 'post')  # 사용할 메소드, 적용할 method이름
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    context_object_name = 'target_user'
    template_name = 'accountapp/delete.html'
