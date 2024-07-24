from django import forms
from .models import voter

class VoteForm(forms.ModelForm):
    class Meta:
        model = voter
        fields = ['vote']