from django.shortcuts import render
from .models import Room


rooms = [
    {'id':1,'name':'Lets learn python!' },
    {'id':2,'name':'Lets learn C!' },
    {'id':3,'name':'Lets learn C++!' },
    ]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)


def room(request, pk):
    return render(request, 'base/room.html')

