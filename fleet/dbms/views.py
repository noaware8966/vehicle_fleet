from django.shortcuts import render

from .models import Order


def home(request):
    orders = Order.objects.select_related('client').all()
    return render(request, 'base.html', {'orders': orders})
