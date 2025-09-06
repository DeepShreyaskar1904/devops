from django.shortcuts import render

def home(req):
    return render(req,"home.html")
# Create your views here.
def sucess(req):
    return render(req,"success.html")