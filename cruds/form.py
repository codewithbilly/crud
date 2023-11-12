from django import forms
from .models import Profile
from django.forms import ModelForm
from django.core import validators


class ProfileCreate(ModelForm):
    FullName = forms.CharField(validators=[validators.MinLengthValidator(5, "Your name can't be less than 6 Characters")],
                               required=False, widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': 'form-control'}))
    Email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={'placeholder': 'E-mail', 'class': 'form-control'}))
    Phone = forms.CharField(validators=[validators.MinLengthValidator(10, "Your password can't be less than 10 Characters")],
                            required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['FullName', 'Email', 'Phone']

    def clean(self):
        # Cleaning the data received from the form
        cleaned_data = super().clean()
        _fname = self.cleaned_data.get('FullName')
        _email = self.cleaned_data.get('Email')
        _phone = self.cleaned_data.get('Phone')

        if _fname == '':
            raise forms.ValidationError('Please enter your full name')
        elif _email == '':
            raise forms.ValidationError("Your E-mail field is required")
        elif _phone == '':
            raise forms.ValidationError(
                'Invalid phone number, please try again')

        return cleaned_data
