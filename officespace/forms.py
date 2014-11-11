from django import forms
from officespace.models import office
from django.contrib.auth.models import User

class Officeform(forms.ModelForm):


    class Meta:
        model = office
        fields = ('location','rent','picture')





