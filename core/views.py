from django.shortcuts import render
from .forms import *
from .models import *


def index(request):
    return render(request, 'core/index.html')
