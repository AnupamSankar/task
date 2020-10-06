from django import forms


class Contacts(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50,
         widget=forms.TextInput(
             attrs={'placeholder': 'Enter your email'}
         ))
    
    phone = forms.CharField(max_length=100,
         widget=forms.TextInput(
             attrs={'placeholder': 'Enter your phone'}
         ))
    
    
    Desc = forms.CharField(max_length=100,
         min_length=20,
         widget=forms.TextInput(
             attrs={'placeholder': 'Enter your tasks here'}
         ))