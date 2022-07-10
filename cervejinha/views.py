from django.shortcuts import render

# Create your views here.

def salgadinho(request):
    return render(request,'cervejinha/base.html')
