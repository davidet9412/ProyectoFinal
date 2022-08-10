from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class NuevoUsuarioForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		help_texts = {k:None for k in fields}


class UserEditForm(forms.ModelForm):

    username = forms.CharField()
    email = forms.EmailField()    

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']
        help_texts = {k:None for k in fields}

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']