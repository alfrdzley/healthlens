from django.shortcuts import render

# Create your views here.

def rekap(request):
    template_name = 'rekap/Rekap.html'
    return render(request,template_name)

def upload(request):
    template_name = 'upload/Upload.html'
    return render(request,template_name)
