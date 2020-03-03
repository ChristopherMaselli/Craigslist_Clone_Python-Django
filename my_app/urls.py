from django.urls import path
from . import views

# Making the URL's to be called by the main-project's URL file
urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
]