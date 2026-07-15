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

from django import forms
from .models import AchatDevises

DEVISES = [
    ('MGA', 'MGA'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
    ('JPY', 'JPY'),
    ('CAD', 'CAD'),
    ('CHF', 'CHF'),
]

class AchatDevisesForm(forms.ModelForm):
    devise = forms.ChoiceField(
        choices=DEVISES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = AchatDevises
        fields = '__all__'