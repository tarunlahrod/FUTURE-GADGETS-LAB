from django.shortcuts import render
import requests
#from w import priceTime

def index(request):
    #cus=priceTime()
    #print(cus)
    
    return render(request, 'eesl/index.html')
    
    

