from django.urls import path
from rest_api.views import hello_word

app_name = 'rest_api'

urlpatterns = [
    path('hello_word',hello_word,name='hello_word_api'),
]