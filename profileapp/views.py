from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from profileapp.decorators import profile_ownership_required
from django.utils.decorators import method_decorator

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('home')
    template_name = 'profileapp/create.html'

    # 템플릿에서 날린 form의 내용이 매개변수 form에 들어가있다.
    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # 실제 DB에 저장이아닌 임시 저장
        temp_profile.user = self.request.user   # user에 현재 로그인중인 user값을 넣어준다.
        temp_profile.save()  # 실제DB에 저장
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    # 성공시 account:detail로 리다이렉트를 시키면서 pk값에 model Profile의 user pk값을 넣어준다
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})