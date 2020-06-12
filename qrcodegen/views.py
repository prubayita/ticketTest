from django.shortcuts import render
# from .models import qrcodegen
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'qrcodegen/code.html', )

# def listing(request):
#     return render(request, 'listings/listing.html')

# def search(request):