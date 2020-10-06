from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

from django.views.decorators.http import require_POST
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from contact.serializers import ContactSerializer
from rest_framework.decorators import api_view


# Create your views here.

def index(request):
    form = ContactForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        new_contact = Contact(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], Desc=request.POST['Desc'])
        new_contact.save()
    return render(request, 'contact/index.html',context)



#def addContact(request):
    #form = ContactForm()
    #context = {'form': form}
    #return render(request, 'contact/index.html', context)
    #if form.is_valid():
        #new_contact = Contact(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], Desc=request.POST['Desc'])
        #new_contact.save()
    #return render(request, 'add',context)
        
@api_view(['GET', 'POST'])
def contactlist(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        
        contact_serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(contact_serializer.data, safe=False)
    
    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
