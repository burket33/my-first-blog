from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=50, required=True, help_text='Required.', widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=50, required=True, help_text='Required.', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(max_length=254, help_text = 'Required. Supply a valid email', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
		widgets = {
			'username': forms.TextInput(attrs = {'class': 'form-control'})
		}
		