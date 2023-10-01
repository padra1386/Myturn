from django.shortcuts import render
from .models import Store
from django.db.models import Q
import logging

# Create your views here.


def homepage(request):
    return render(request, 'base/home.html')


def appPage(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    print(q)

    stores_query = Store.objects.filter(
        Q(name__icontains=q)
    )
    context = {'stores_all': stores_query}
    return render(request, 'base/app.html', context)
