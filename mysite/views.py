from django.shortcuts import render

def index(request):
    template_url = "index.html"
    return render(request,template_url)

def rekap(request):
    template_name = 'index.html'
    return render(request,template_name)