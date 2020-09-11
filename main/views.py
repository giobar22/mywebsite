from .models import *
from django.views.generic import ListView, DetailView

class GamesListView(ListView):
    model = GameNews
    template_name = 'main/index.html'
    context_object_name = 'games'
    ordering = ['-id']
    paginate_by = 1



class GamesDetailView(DetailView):
    model = GameNews
    template_name = 'main/game_news.html'

class CategoryDetailView(DetailView):
    model = GameNews
    template_name = 'main/category.html'
