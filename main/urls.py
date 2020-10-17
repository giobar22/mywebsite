from django.urls import path
from . views import GamesListView, UpComingGamesListView, UpComingGamesDetailView, HotNewsListView

from . import views

urlpatterns = [
    path('', GamesListView.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('upcoming/', UpComingGamesListView.as_view(), name='upcoming'),
    path('upcoming/<int:pk>/', UpComingGamesDetailView.as_view(), name='upcoming_details'),
    path('game/<int:id>/', views.GamesDetailView, name='game_details'),
    path('category/<int:id>/', views.category_news, name='category_news'),
    path('favourite_game/<int:id>/', views.favourite_game, name='favourite_game'),
    path('hot_news/', HotNewsListView.as_view(), name='hot_news'),
    path('like/', views.like, name='like'),
    path('favourites/', views.game_favourite_list, name='game_favourite_list'),
    path('popular/', views.popular_games, name='popular'),
]
