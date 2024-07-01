from django.shortcuts import render
from ecomm_app.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"we recieved your request, so we will get back to you soon..")
        return render(request,"contact.html")


    return render(request,"contact.html")
