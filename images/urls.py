from django.urls import path

from .views import show
from .views import delete
from .views import create
from .views import update
from .views import download

from .views import search

from .views import delete_many
from .views import download_many

app_name = 'images'

urlpatterns = [
    path('create/', create, name='create'),
    path('show/<int:pk>/', show, name='show'),
    path('delete/<int:pk>', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
    path('download/<int:pk>', download, name='download'),

    path('search', search, name='search'),

    path('delete/many', delete_many, name='delete_many'),
    path('download/many', download_many, name='download_many')
]
