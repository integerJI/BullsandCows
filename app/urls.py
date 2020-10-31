from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('gameroom/<int:game_id>', views.gameroom, name='gameroom'),
    path('gamecreate/', views.gamecreate, name='gamecreate'),
    path('choicenum/<int:game_id>', views.choicenum, name="choicenum"),
    path('beatnum/<int:game_id>', views.beatnum, name="beatnum"),
    # path('gamenum/<int:game_id>', views.gamenum, name="gamenum"),
    # path('gametrynum/<int:game_id>', views.gametrynum, name="gametrynum"),
]
