from django.urls import path

from . import views

app_name = "accountapp"
urlpatterns = [
  path('hello_world/', views.index, name='index'),
  path('create/', views.AcouuntCreateView.as_view(), name='create'),
]