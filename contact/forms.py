from django import forms
#from django.forms import ModelForm
from .models import Contact
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def lencheck(x):
    return len(x)==10 



class ContactForm(forms.Form):
    
    
    
    
    name = forms.CharField(label='Your Name',
                           max_length=100,
                           min_length=3,
                           widget=forms.TextInput(attrs={'class':"input",'placeholder':"Name"})
                          )
    email = forms.CharField(label='Your Email',
                            validators = [validate_email],
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
                           widget=forms.TextInput(attrs={'class':"input",'placeholder':"Description"})
                          )
    
    
    
    
    #def validateEmail(email):
    #try:
        #validate_email(email)
        #return True
    #except ValidationError:
        #return False
        
    

#class ContactForm(ModelForm):
    #class Meta:
        #model = Contact
        #fields = '__all__'