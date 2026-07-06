from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AchatDevises

class CustomUserCreationForm(UserCreationForm):
    password1= forms.CharField(
        label="Password",
        strip = False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),

    )
    password2= forms.CharField(
        label="Confirm Password",
        strip= False,
        widget= forms.PasswordInput(attrs={'autocomplete':'new-password'})
    )
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1","password2")

class AchatDevisesForm(forms.ModelForm):
    class Meta:
        model = AchatDevises
        fields = "__all__"