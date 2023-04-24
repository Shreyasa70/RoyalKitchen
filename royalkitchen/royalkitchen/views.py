from django.shortcuts import render,HttpResponse
from members.models import Contact

# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    return render(request,'index.html')

def menus(request):
    return render(request,'menus.html')

def aboutus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc)
        contact.save()
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')