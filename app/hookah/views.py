from django.shortcuts import render


def home_page(request):
    return render(request, 'hookah/home.html')


def nohome_page(request):
    return render(request, 'hookah/nohome.html')