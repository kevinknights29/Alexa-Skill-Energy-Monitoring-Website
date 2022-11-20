from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request=request, template_name="home.html")


def privacy(request):
    return render(request=request, template_name="privacy.html")
