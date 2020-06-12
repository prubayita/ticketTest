from django.shortcuts import render
#from .models import Ticket
from django.http import HttpResponse
# Create your views here.
def ticket(request):
    return render(request, 'tickets/ticket.html')

def search(request):
    return render(request, 'tickets/search.html')
