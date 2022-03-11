
from django import forms
from .models import Member

class MemberShipForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=["name","cnic","phone","package"]