from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Match(models.Model):
    id_match = models.AutoField(primary_key=True)
    match_name = models.CharField(max_length=50)
    number_players = models.IntegerField(verbose_name='Number of players playing', null=True, blank=True, default=5)

    class Meta:
        db_table = 'match'

    def __str__(self):
        return self.match_name


TYPE_PLAYERS = [
    ('GOALKEEPER', 'goalkeeper'),
    ('DEFENDER', 'Defender'),
    ('MIDFIELD', 'Midfield'),
    ('STRIKER', 'Striker'),
]


class Player(models.Model):
    id_player = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=50)
    stars = models.IntegerField(default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    type_player = models.CharField(max_length=15, choices=TYPE_PLAYERS, default='Defender')
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    class Meta:
        db_table = 'player'

    def __str__(self):
        return self.player_name