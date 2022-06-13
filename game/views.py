from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import homes, output, load
from .forms import *
from .game import Game
from .models import *


def game(request):
    if request.method == 'POST':
        print(request.POST['moves'])
        moves = AddMoves(request.POST)
        if moves.is_valid():
            try:
                Players.moves.create(**moves.cleaned_data)
                # moves = Players.moves
                # lst = []
                # for i in moves:
                #     lst.append(int(i))
                # numbers = Game.is_value(lst[0], lst[1], lst[2], lst[3])
                return redirect('game')
            except:
                moves.add_error(None, 'Ты ошибка при добавлении')
    else:
        moves = AddMoves()
    return render(request, 'mad/game.html', {'moves': moves, 'title': 'Game Page'})


def desk(request):
    champions = Players.objects.all()
    return render(request, 'mad/desk.html', {'champions': champions, 'title': 'Desk Page'})


def home(request):
    return render(request, 'mad/home.html', {'title': 'Home Page'})


def show_moves(request):
    champions = Players.objects.all()
    return render(request, 'mad/moves.html', {'champions': champions, 'title': 'Moves History'})


# def generate_home(request):
#     if request.method == 'POST':
#         real_home = request.POST
#         return render(request, 'mad/for_glory.html', {'real_home': real_home, 'title': 'Preparation'})
#     else:
#         return render(request, 'mad/generate_home.html', {'title': 'Preparation'})


def for_glory(request):
    if request.method == 'POST':
        moves = request.POST['moves']
        home = request.POST['real_home']
        form = AddWinner(request.POST)
        lst_home = []
        lst_moves = []
        for i in home:
            lst_home.append(i)
        for i in moves:
            lst_moves.append(i)
        # my_numbers = Game.is_value(int(lst_moves[0]), int(lst_moves[1]), int(lst_moves[2]), int(lst_moves[3]))
        # myHome = homes.Homes.get_home(my_numbers)
        # prep_numbers = Game.is_value(int(lst_home[0]), int(lst_home[1]), int(lst_home[2]), int(lst_home[3]))
        # realHome = homes.Homes.get_home(prep_numbers)
        counter_name_1 = 0
        counter_name_2 = 0
        for real_position in range(len(lst_home)):
            for my_position in range(len(lst_moves)):
                if real_position == my_position:
                    if lst_home[real_position] == lst_moves[my_position]:
                        counter_name_1 += 1
                        break
                    else:
                        if lst_home[real_position] == lst_moves[my_position]:
                            counter_name_2 += 1
                            break
                else:
                    if lst_home[real_position] == lst_moves[my_position]:
                        counter_name_2 += 1
                        break
        counter_name_3 = 4 - counter_name_1 - counter_name_2
        toOutput = output.Output('Блатных', 'Мужиков', 'Чертей', counter_name_1, counter_name_2, counter_name_3)
        result = output.Output.get_output(toOutput)
        if counter_name_1 != 4:
            # text = str(myHome)
            load.Load.write(str(lst_home))
            return render(request, 'mad/for_glory.html',
                          {'moves': moves, 'result': result, 'form': form, 'title': 'For Glory Page'})
        else:
            # text = str(myHome)
            load.Load.write(str(lst_home))
            end = output.Output.end()
            return render(request, 'mad/end.html',
                          {'moves': moves, 'result': result, 'end': end, 'title': 'Victory'})
        # if form.is_valid():
        #     try:
        #         Players.objects.create(**form.cleaned_data)
        #         return render(request, 'mad/for_glory.html',
        #                   {'moves': moves, 'result': result, 'form': form, 'title': 'For Glory Page'})
        #     except:
        #         form.add_error(None, 'Ты ошибка при добавлении')
    else:
        form = AddWinner()
    return render(request, 'mad/for_glory.html', {'form': form, 'title': 'For Glory Page'})


def end(request):
    return render(request, 'mad/end.html', {'title': 'Victory'})
