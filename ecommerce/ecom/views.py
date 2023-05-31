from django.shortcuts import render
from . models import Products 
def index(request):

    items = Products.objects.all()
    
    return render(request, 'index.html', {'items': items})
