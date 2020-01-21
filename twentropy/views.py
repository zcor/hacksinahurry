from django.shortcuts import render
from twentropy.models import Tweet
# Create your views here.
from django.http import HttpResponse
import twitter
import time

def home(request):
        return HttpResponse("Hello, world.")

def index(request):
        return HttpResponse("Hello, world.")

def insights(request):
        return HttpResponse("Hello, world.")

def scrape(request):
        return HttpResponse("Hello, world.")

