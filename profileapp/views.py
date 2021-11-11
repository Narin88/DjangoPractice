from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:index')
    template_name = 'profileapp/create.html'

    # 템플릿에서 날린 form의 내용이 매개변수 form에 들어가있다.
    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # 실제 DB에 저장이아닌 임시 저장
        temp_profile.user = self.request.user   # user에 현재 로그인중인 user값을 넣어준다.
        temp_profile.save()  # 실제DB에 저장

        return super().form_valid(form)