from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('gameroom/<int:game_id>', views.gameroom, name='gameroom'),
    path('gamecreate/', views.gamecreate, name='gamecreate'),
    path('gamenum/<int:game_id>', views.gamenum, name="gamenum"),
]
