from django.shortcuts import render

def index(request):
    """Домашняя страница приложения Pizzeria"""
    return render(request, 'pizzas/index.html')
