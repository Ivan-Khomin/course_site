from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'id': 'usernameInput'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'id': 'passwordInput'
    }))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'usernameInput'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'id': 'passwordInput'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'firstNameInput'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'lastNameInput'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'id': 'emailInput'
            })
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'usernameInput'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'firstNameInput'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'lastNameInput'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'id': 'emailInput'
            })
        }
