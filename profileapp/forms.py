from django.forms import ModelForm

from profileapp import models


class ProfileCreationForm(ModelForm):
    class Meta:
        model = models.Profile
        field = ['image', 'nickname', 'message']
