from django.shortcuts import render
from django.http import HttpResponse
from .forms import Contacts

from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    return render(request, 'contact/index.html')


@require_POST
def addContact(request):
    form = Contacts(request.POST)
    if form.is_valid():
        new_contact = Contact(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], Desc=request.POST['Desc'])
        new_contact.save()