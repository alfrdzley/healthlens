from django.shortcuts import render

def index(request):
    template_url = "index.html"
    return render(request,template_url)