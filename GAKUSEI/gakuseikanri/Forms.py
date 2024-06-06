from django import forms
from gakuseikanri.models import Gakuseikanri
from django.forms import fields
class GakuseikanriForm(forms.ModelForm):
    class Meta:
        model = Gakuseikanri
        fields = "__all__"