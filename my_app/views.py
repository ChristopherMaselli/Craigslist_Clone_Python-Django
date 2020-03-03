import requests
from django.shortcuts import render
from bs4 import BeautifulSoup


# Create your views here.

# Making our Home-Page request which calls the base.html file
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search') # Gets the search variable from the python dictionary. is then POSTING the
    # result!
    print(search)
    stuff_for_frontend = {'search': search,}
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
