from django.urls import path
from django.conf.urls import url
from . views import GamesDetailView, GamesListView, UpComingGamesListView,UpComingGamesDetailView

from . import views

urlpatterns = [
    path('', GamesListView.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('search_auto/',views.search_auto, name='search_auto'),
    path('upcoming/',UpComingGamesListView.as_view(), name='upcoming'),
    path('upcoming/<int:pk>/',UpComingGamesDetailView.as_view(), name='upcoming_details'),
    path('game/<int:pk>/', GamesDetailView.as_view(), name='game_details'),
    path('category/<int:id>/', views.category_news, name='category_news'),
    path('hot_news/', views.hot_news, name='hot_news')
]
