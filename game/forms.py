from django import forms
from .models import *


class AddWinner(forms.Form):
    name = forms.CharField(max_length=255, label='Как кличут')
    sex = forms.CharField(max_length=255, label='Кто по жизни')
    years_old = forms.IntegerField(label='Сколько носит')
    real_home = forms.CharField(max_length=255, label='Исходное число')
    moves = forms.CharField(max_length=255, label='Ходи сюда')


class AddMoves(forms.Form):
    moves = forms.CharField(max_length=255, label='Ходи сюда')
