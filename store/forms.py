from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.models import fields_for_model
from django.forms.widgets import PasswordInput

class CreateUserForm(UserCreationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'})   
        }
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class':'form-control', 'placeholder':'password'})
        self.fields['password2'].widget = PasswordInput(attrs={'class':'form-control', 'placeholder':'confirm your password'})
 

        