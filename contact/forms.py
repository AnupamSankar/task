from django import forms
#from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name',
                           max_length=100,
                           min_length=3,
                           widget=forms.TextInput(attrs={'class':"input",'placeholder':"Name"})
                          )
    email = forms.CharField(label='Your Email',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class':"input",'placeholder':"email"})
                          )
    phone = forms.CharField(label='Phone',
                           max_length=10,
                            min_length = 10,
                            required = False,
                           widget=forms.TextInput(attrs={'class':"input",'placeholder':"Contact"})
                          )
    Desc = forms.CharField(label='Description',
                           max_length=100,
                           min_length=20,
                           widget=forms.TextInput(attrs={'class':"input"})
                          )
    

#class ContactForm(ModelForm):
    #class Meta:
        #model = Contact
        #fields = '__all__'