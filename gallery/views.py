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
