from django import forms
from app1.models import Marks
class MarksForm(forms.ModelForm):
    class Meta:
        model=Marks
        fields="__all__"