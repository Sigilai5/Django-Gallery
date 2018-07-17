from django.shortcuts import render
from  .models import *

# Create your views here.
def home(request):
    image = Image.objects.all()

    return render(request,'home.html',locals())
'''

    locals() --> generates a dictionary containing all 

    		variables in the current scope



    # further explore

    globals()

    '''
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def get_location(request,location):
    image = Image.filter_location(location)
    return render(request,'location.html',locals())
