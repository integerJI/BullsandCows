from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import GameRomm, ChoiceNum, BeatNum

@login_required
def index(request):
    games = GameRomm.objects.order_by('-id')
    return render(request, 'index.html', {'games': games})

@login_required
def gameroom(request, game_id):
    game = get_object_or_404(GameRomm, pk=game_id)
    return render(request, 'gameroom.html', {'game': game})

@login_required
def gamecreate(request):
    game = GameRomm()
    game.game_title = request.user.get_username()+'의 게임'
    game.game_status = True
    game.game_date = timezone.datetime.now()
    game.save()
    return redirect('/app/gameroom/' + str(game.id))

@login_required
def choicenum(request, game_id):
    if request.method =='POST':
        choice = get_object_or_404(GameRomm, pk=game_id)
        choice_user = User.objects.get(username = request.user.get_username())
        choice_num = request.POST.get('choice_num')
        ChoiceNum.objects.create(choice=choice, choice_user=choice_user, choice_num=choice_num)
        return redirect('gameroom', game_id)


@login_required
def beatnum(request, game_id, choicenum_id):
    list_choice = []
    list_beat = []
    strike = 0
    ball = 0

    if request.method =='POST':
        beat = get_object_or_404(ChoiceNum, pk=choicenum_id)

        str_choice = str(beat)
        str_choice = str_choice[-4:]

        for i in range(len(str_choice)):
            list_choice.append(str_choice[i])
        
        str_beat = str(request.POST.get('beat_num'))

        for j in range(len(str_beat)):
            list_beat.append(str_beat[j])

        for k in range(4):
            if list_choice[k] == list_beat[k]:
                strike += 1
            if (list_choice[k] in list_beat) and (list_choice[k] != list_beat[k]):
                ball += 1

        beat_user = User.objects.get(username = request.user.get_username())
        beat_num = request.POST.get('beat_num')
        beat_result = strike, ball
        BeatNum.objects.create(beat=beat, beat_user=beat_user, beat_num=beat_num, beat_result=beat_result)
        return redirect('gameroom', game_id)
