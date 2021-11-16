from django.urls import reverse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin
from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from projectapp.models import Project
from subscribeapp.models import Subscription

# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
  model = Project
  form_class = ProjectCreationForm
  template_name = 'projectapp/create.html'

  def get_success_url(self) -> str:
      return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

# MultipleObjectMixin: 여러가지 object를 다룰수 있게 만들어주는 것
class ProjectDetailView(DetailView, MultipleObjectMixin):
  model = Project
  context_object_name = 'target_project'
  template_name = 'projectapp/detail.html'

  paginate_by = 25

  def get_context_data(self, **kwargs):
    project = self.object
    user = self.request.user

    if user.is_authenticated:
      subscription = Subscription.objects.filter(user=user, project=project)

    object_list = Article.objects.filter(project=self.get_object())
    return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription, **kwargs)


class ProjectListView(ListView):
  model = Project
  context_object_name = 'project_list'
  template_name = 'projectapp/list.html'
  paginate_by = 25