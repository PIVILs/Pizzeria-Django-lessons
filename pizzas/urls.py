"""Определяет схемы URL для pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),

    # Вывод всех товаров.
    path('pizzas/', views.pizzas, name='pizzas' ),

    # Страница с подробной информацией по товару
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]