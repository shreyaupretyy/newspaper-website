from django.shortcuts import render, redirect
import requests
import json
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=us&apiKey=14983dc85e2b44749f046531919619cb")
    api = json.loads(news_api.content)
    return render(request, 'home.html', {'api': api})


def bnews(request):
    b_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=14983dc85e2b44749f046531919619cb")
    b_api = json.loads(b_news_api.content)

    return render(request, 'bnews.html', {'b_api': b_api})


def enews(request):
    e_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=14983dc85e2b44749f046531919619cb")
    e_api = json.loads(e_news_api.content)

    return render(request, 'enews.html', {'e_api': e_api})


def hnews(request):
    h_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=14983dc85e2b44749f046531919619cb")
    h_api = json.loads(h_news_api.content)

    return render(request, 'hnews.html', {'h_api': h_api})


def scnews(request):
    sc_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=14983dc85e2b44749f046531919619cb")
    sc_api = json.loads(sc_news_api.content)

    return render(request, 'scnews.html', {'sc_api': sc_api})


def snews(request):
    s_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=14983dc85e2b44749f046531919619cb")
    s_api = json.loads(s_news_api.content)

    return render(request, 'snews.html', {'s_api': s_api})


def tnews(request):
    t_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=14983dc85e2b44749f046531919619cb")
    t_api = json.loads(t_news_api.content)

    return render(request, 'tnews.html', {'t_api': t_api})


    










