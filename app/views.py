from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import GameRomm

def index(request):
    games = GameRomm.objects.order_by('-id')
    return render(request, 'index.html', {'games': games})

def gameroom(request, game_id):
    game = get_object_or_404(GameRomm, pk=game_id)
    return render(request, 'gameroom.html', {'game': game})

def gamecreate(request):
    game = GameRomm()
    game.game_title = '게임'
    game.game_status = True
    game.game_date = timezone.datetime.now()
    game.save()
    return redirect('/app/gameroom/' + str(game.id))
