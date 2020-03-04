import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models


BASE_CRAIGSLIST_URL = 'https://newyork.craigslist.org/search/?query={}'
# Create your views here.

# Making our Home-Page request which calls the base.html file
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search') # Gets the search variable from the python dictionary. is then POSTING the
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    # print(final_url)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})

    #post_title = post_listings[0].find(class_='result-title').text
    #post_url = post_listings[0].find('a').get('href')
    #post_price = post_listings[0].find(class_='result-price').text

    #print(post_title)
    #print(post_url)
    #print(post_price)

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        post_price = post.find(class_='result-price').text

        final_postings.append((post_title, post_url, post_price))


    # print(post_titles[0].text)
    #post_title = soup.find_all("a", {'class': 'result-title'})
    # print(post_titles[0].get('href'))
    # print(data)
    # result!

    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
    }

    return render(request, 'my_app/new_search.html', stuff_for_frontend)
 