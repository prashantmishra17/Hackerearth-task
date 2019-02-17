from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.contrib.auth.models import User
from django.urls import reverse
from .models import WineCollection


def wines(request):
    wine_collection = WineCollection.objects.all()
    context_dict={'wine_collection':wine_collection}
    return render(request, 'index.html', context_dict)
