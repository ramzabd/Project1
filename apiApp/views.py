from django.shortcuts import render
from .serilazers import ContactListAPIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from apiApp.models import Contact

# Create your views here.


class ContactList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListAPIView

class ContactCreate(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListAPIView

class ContactUpdate(RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListAPIView

class ContactDelete(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListAPIView
