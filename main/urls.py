from django.urls import path
from . views import GamesDetailView, GamesListView, CategoryDetailView

urlpatterns = [
    path('', GamesListView.as_view(), name='home'),
    path('game/<int:pk>/', GamesDetailView.as_view(), name='game_details'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='games_category')
]
