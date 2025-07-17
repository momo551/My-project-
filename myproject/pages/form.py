from django import forms
from .models import Login


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=False)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True)

class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username','email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }