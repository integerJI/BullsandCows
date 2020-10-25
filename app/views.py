from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import GameRomm, GameNum

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

@login_required
def gamenum(request, game_id):
    if request.method =='POST':
        game = get_object_or_404(GameRomm, pk=game_id)
        game_user = User.objects.get(username = request.user.get_username())
        game_num = request.POST.get('game_num')
        GameNum.objects.create(game=game, game_user=game_user, game_num=game_num)
        return redirect('gameroom', game_id)
