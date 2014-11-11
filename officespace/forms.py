from django import forms
from officespace.models import office
from django.contrib.auth.models import User

class Officeform(forms.ModelForm):
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'size':'40'}))
    class Meta:
        model = office
        fields = ('location','rent', 'description', 'picture')





