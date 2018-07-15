from django.shortcuts import render
from  .models import Image

# Create your views here.
def home(request):
    image = Image.get_image()
    return render(request,'base.html.html',{"image":image})
