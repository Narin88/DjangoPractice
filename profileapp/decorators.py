from django.http import HttpResponseForbidden

from profileapp.views import Profile

def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # user = pk로 받은 값을 가지고 있는 UserObject
        profile = Profile.objects.get(pk=kwargs['pk'])
        # pk값으로 가져온 유저와 현재 리퀘스트를 보낸 로그인한 유저가 다르다면
        if not profile.user == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated