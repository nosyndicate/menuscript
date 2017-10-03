import logging
import json
import os

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.conf import settings

from .models import Greeting
from .forms import DishForm

logger = logging.getLogger('default')

def index(request):
    if request.method == 'POST':
        form = DishForm(request.POST, dishes=load_menu())
        if form.is_valid():
            logging.info('valid it')
    else: 
        form = DishForm(dishes=load_menu())

    return render_to_response('index.html', {'form': form})            


def load_menu():
    logger.info(settings.PROJECT_ROOT)
    file_path = os.path.join(settings.PROJECT_ROOT, 'menu.json')
    logger.info(file_path)
    with open(file_path, 'rb') as json_file:
        menu_json_string = json_file.read().decode('utf-8')
        data = json.loads(menu_json_string)

    return data

# Create your views here.
# def index(request):
#     # return HttpResponse('Hello from Python!')
#     load_menu()
#     return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})