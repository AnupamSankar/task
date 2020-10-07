from django.urls import path
from .import views
from django.conf.urls import url


urlpatterns = [
    #path('add',views.addContact,name='add'),
    path('details',views.details,name='details'),
    path('',views.index,name='index'),
    url(r'^list$', views.contactlist),
    path('add',views.addContact,name='add')
    
    #path('add', views.addContact, name='add'),
]