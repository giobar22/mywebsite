from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView
from users.models import Comment
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from users.forms import CommentForm
import json
from django.template.loader import render_to_string
import random


class GamesListView(ListView):
    model = GameNews
    template_name = 'main/home.html'
    context_object_name = 'games'
    ordering = ['-id']
    paginate_by = 5


class UpComingGamesListView(ListView):
    model = UpComingGames
    template_name = 'main/upcoming.html'
    context_object_name = 'upcoming_games'
    ordering = ['-id']
    paginate_by = 1


class UpComingGamesDetailView(DetailView):
    model = UpComingGames
    template_name = 'main/upcoming_details.html'


def GamesDetailView(request, id):
    games = get_object_or_404(GameNews, id=id)
    games.games_view = games.games_view + 1
    games.save()
    is_liked = False
    is_favourite = False
    if games.likes.filter(id=request.user.id).exists():
        is_liked = True
    if games.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    comments = Comment.objects.filter(news=games, reply=None).order_by('-id')
    category = Genre.objects.filter(pk=id)
    random_news = list(GameNews.objects.filter(genres__in=list(category)))
    randoms = random.sample(random_news, 0)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(news=games, user=request.user.profile, content=content, reply=comment_qs)
            comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'randoms': randoms,
        'games': games,
        'comment': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'total_likes': games.total_likes(),
        'is_favourite': is_favourite
    }
    if request.is_ajax():
        html = render_to_string('main/comments.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'main/game_news.html', context)


def categories(request):
    categories = Genre.objects.all().order_by('genre')
    return {"categories": categories}


def category_news(request, id):
    category = Genre.objects.filter(pk=id)
    games = GameNews.objects.filter(genres__in=list(category)).order_by('-id')
    paginator = Paginator(games, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': category,
        'page_obj': page_obj
    }
    return render(request, 'main/home.html', context)


class HotNewsListView(ListView):
    model = GameNews
    template_name = 'main/home.html'
    context_object_name = 'games'
    ordering = ['-id']
    paginate_by = 1

    def get_queryset(self):
        filter = GameNews.objects.filter(Hot_News=True).order_by('-id')
        return filter


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', 'None')
        games = GameNews.objects.filter(title__icontains=q)
        results = []
        for pl in games:
            games_json = pl.title
            results.append(games_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def search(request):
    game_list = GameNews.objects.all()
    query = request.GET.get('q')
    if query:
        game_list = GameNews.objects.filter(
            Q(title__icontains=query)
        ).order_by('-id').distinct()
    paginator = Paginator(game_list, 1)
    page = request.GET.get('page')

    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

    context = {
        'page_obj': games
    }
    return render(request, "main/home.html", context)


def logo(request):
    logo = Logo.objects.all()
    return {"logo": logo}


def favourite_game(request, id):
    game = get_object_or_404(GameNews, id=id)
    if game.favourite.filter(id=request.user.id).exists():
        game.favourite.remove(request.user)
    else:
        game.favourite.add(request.user)
    return HttpResponseRedirect(game.get_absolute_url())


def like(request):
    news = get_object_or_404(GameNews, id=request.POST.get('id'))
    is_liked = False
    if news.likes.filter(id=request.user.id).exists():
        news.likes.remove(request.user)
        is_liked = False
    else:
        news.likes.add(request.user)
        is_liked = True
    context = {
        'games': news,
        'is_liked': is_liked,
        'total_likes': news.total_likes()
    }
    if request.is_ajax():
        html = render_to_string('main/like_section.html', context, request=request)
        return JsonResponse({'form': html})


def game_favourite_list(request):
    user = request.user
    favourite_games = user.favourite.all().order_by('-id')
    context = {
        'favourite_games': favourite_games
    }
    return render(request, 'users/game_favourite_list.html', context)


def top_like_games(request):
    like_games = GameNews.objects.all().annotate(count=Count('likes')).order_by('-count')[:6]
    print(like_games)
    return {'like_games': like_games}


def popular_games(request):
    popular = GameNews.objects.all().order_by('-games_view')
    paginator = Paginator(popular, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'main/home.html', context)
