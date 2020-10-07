from django import forms
#from django.forms import ModelForm
from .models import Contact
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import string


def lencheck(x):
    return (len(x)==10 or Null)

#def namecheck(y):
 #   return isalpha(y)
    


class ContactForm(forms.Form):
    
 #   def clean_name(self):
  #      Name = self.cleaned_data.get('name')
   #     if not namecheck(Name):
    #       raise forms.ValidationError('no numbers in name')
     #   return Name
    
    
    
    
    name = forms.CharField(label='Your Name',
                           max_length=100,
                           min_length=3,
                           #validators = [clean_name],
                           widget=forms.TextInput(attrs={'class':"input",'placeholder':"Name"})
                          )
    email = forms.CharField(label='Your Email',
                            validators = [validate_email],
                           max_length=100,
                           widget=forms.TextInput(attrs={'class':"input",'placeholder':"email"})
                          )
    phone = forms.IntegerField(label='Phone',
                           min_value=1000000000,
                           max_value=9999999999,
                            required = False,
                           widget=forms.TextInput(attrs={'class':"input",'placeholder':"Contact"})
                          )
    Desc = forms.CharField(label='Description',
                           max_length=100,
                           min_length=20,
                           widget=forms.TextInput(attrs={'class':"input",'placeholder':"Description"})
                          )
    
    
    #def clean_phone(self):
        #data = self.cleaned_data.get('phone')
        #if not lencheck(data):
          #  raise forms.ValidationError('enter a 10 digit value')
        
        #return data
    
    
    
    #here
    class Meta:
        model = Contact
        fields = ("__all__")
        
        
    
    
    
    #def validateEmail(email):
    #try:
        #validate_email(email)
        #return True
    #except ValidationError:
        #return False
        
    

