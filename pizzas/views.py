from django.shortcuts import render
from .models import Pizza

def index(request):
    """Домашняя страница приложения Pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Выводит список пицц."""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Выводит одну пиццу и всю по ней информацию."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)