from django.forms import ModelForm
from . import models


class MatchForm(ModelForm):
    class Meta:
        model = models.Match
        fields = ['match_name']


class PlayerForm(ModelForm):
    class Meta:
        model = models.Player
        fields = ['player_name']


class EditPlayerForm(ModelForm):
    class Meta:
        model = models.Player
        fields = ['player_name', 'stars', 'type_player']


class EditMatchForm(ModelForm):
    class Meta:
        model = models.Match
        fields = ['match_name', 'number_players']
