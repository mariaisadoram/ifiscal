from django.shortcuts import render

# Create your views here.

def galCamera(request):
    return render(request, "galeria-cameras.html")

def galFotos(request):
    return render(request, "galeria-fotos.html")

def camera(request):
    return render(request, "camera.html")

def picture(request):
    return render(request, "picture.html")

def estat(request):
    return render(request, "estatisticas.html")