from django.urls import path

from subscribeapp.views import SubScriptionView

app_name = 'subscribeapp'

urlpatterns = [
  path('subscribe/', SubScriptionView.as_view(), name='subscribe')
]