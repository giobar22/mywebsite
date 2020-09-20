from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.http import HttpResponse
import json

class GamesListView(ListView):
    model = GameNews
    template_name = 'main/home.html'
    context_object_name = 'games'
    ordering = ['-id']
    paginate_by = 1


class UpComingGamesListView(ListView):
    model = UpComingGames
    template_name = 'main/upcoming.html'
    context_object_name = 'upcoming_games'
    ordering = ['-id']
    paginate_by = 1

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        games = GameNews.objects.all().filter(Q(title__icontains=search)).order_by('-id')
        context = {
            'games':games
        }
        if len(search) < 2:
            return render(request, 'main/empty.html', context)
        else:
            return render(request, 'main/home.html', context)




class UpComingGamesDetailView(DetailView):
    model = UpComingGames
    template_name = 'main/upcoming_details.html'

class GamesDetailView(DetailView):
    model = GameNews
    template_name = 'main/game_news.html'

def categories(request):
    categories = Genre.objects.all()
    return {"categories": categories}

def category_news(request, id):
    category = Genre.objects.filter(pk=id)
    games = GameNews.objects.filter(genres__in=list(category)).order_by('-id')
    context = {
        'games':games,
        'category':category
    }
    return render(request, 'main/home.html', context)

def hot_news(request):
    games = GameNews.objects.filter(Hot_News = True).order_by('-id')
    context = {
        'games':games
    }
    if games:
        return render(request, 'main/home.html',context)
    else:
        return render(request, 'main/empty.html')



def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    games = GameNews.objects.filter(title__icontains=q)
    results = []
    for pl in games:
      games_json = {}
      games_json = pl.title
      results.append(games_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

