from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email= forms.EmailField(
        max_length=254,
        help_text='Requierd. Fill with a valid email address.'
    )

    bio = forms.CharField(max_length=500, required=False, help_text='Optional.')
    
    location = forms.CharField(max_length=30, required=False, help_text='Optional.')

    birth_date = forms.DateField(input_formats=['%d/%m/%Y'], required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
         'password2', 'bio', 'location', 'birth_date')