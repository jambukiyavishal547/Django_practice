from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    for p in PeopleAddress.objects.all().select_related('people')[0:2]:
        # print(p.address)
        print(p.people.name)
        return

def hom(request):
    for j in People.objects.all().prefetch_related('colors'):
        print(j.colors.name)
        return