from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'}))
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe prueba con otro")
        return email
    
class ProfileForm(forms.ModelForm):
     class Meta:
         model=Profile
         fields=['avatar','bio','link']
         widgets={
             'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mb-2'}),
             'bio':forms.Textarea(attrs={'class':'form-control mb-2','rows':3, 'placeholder': 'Biografia'}),
             'link':forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Link'}),
             
         }
         
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'}))
    class Meta:
        model = User
        fields = ['email']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
               raise forms.ValidationError("El email ya existe prueba con otro")
        return email   
             