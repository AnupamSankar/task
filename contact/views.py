from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    form = ContactForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        new_contact = Contact(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], Desc=request.POST['Desc'])
        new_contact.save()
    return redirect('contact/index.html')



#def addContact(request):
    #form = ContactForm()
    #context = {'form': form}
    #return render(request, 'contact/index.html', context)
    #if form.is_valid():
        #new_contact = Contact(name=request.POST['name'], email=request.POST['email'], #phone=request.POST['phone'], Desc=request.POST['Desc'])
        #new_contact.save()