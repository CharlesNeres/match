from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import MatchForm, PlayerForm, EditPlayerForm, EditMatchForm
from . import models
from django.contrib import messages
from django.db.models import Count


def home(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Match successfully added!')
            return redirect('home')
    else:
        form = MatchForm()

    matchs = models.Match.objects.all().order_by('-match_name')

    page_obj = paginator(request, matchs)

    context = {'form': form, 'page_obj': page_obj}

    return render(request, 'base/home.html', context=context)


def match_detail(request, pk):
    match = models.Match.objects.get(pk=pk)

    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():
            player = form.save(commit=False)
            player.match = match
            player.save()
            return redirect('match_detail', pk)
    else:
        form = PlayerForm()

    players = models.Player.objects.filter(match=match).order_by('-player_name')

    page_obj = paginator(request, players)

    context = {
        'match': match,
        'form': form,
        'players': players,
        'page_obj': page_obj
    }

    return render(request, 'base/match_detail.html', context=context)


def edit_match(request, pk):
    match = models.Match.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditMatchForm(request.POST, instance=match)

        if form.is_valid():
            form.save()
            messages.success(request, 'Match {} successfully updated!'.format(match.match_name))
            return redirect('home')
    else:
        form = EditMatchForm(instance=match)

    context = {'match': match, 'form': form}

    return render(request, 'base/edit_match.html', context=context)


def delete_match(request, pk):
    match = models.Match.objects.get(pk=pk)
    if request.method == 'POST':
        match.delete()
        messages.success(request, 'Match {} successfully removed!'.format(match.match_name))
        return redirect('home')

    context = {'match': match}

    return render(request, 'base/delete_match.html', context=context)


def delete_player(request, pk):
    player = models.Player.objects.get(pk=pk)
    if request.method == 'POST':
        player.delete()
        messages.success(request, 'Player {} successfully removed!'.format(player.player_name))
        return redirect('match_detail', player.match.pk)

    context = {'player': player}
    return render(request, 'base/delete_player.html', context=context)


def edit_player(request, pk):
    player = models.Player.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditPlayerForm(request.POST, instance=player)

        if form.is_valid():
            form.save()
            return redirect('match_detail', player.match.pk)
    else:
        form = EditPlayerForm(instance=player)

    context = {'player': player, 'form': form}

    return render(request, 'base/edit_player.html', context=context)


def paginator(request, model):
    paginator = Paginator(model, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj


def generate_team(request, pk):
    import random

    match = models.Match.objects.get(pk=pk)
    players = models.Player.objects.filter(match=match)
    players = list(players)

    random.shuffle(players)

    if len(players) > match.number_players:
        team1 = players[:match.number_players]
        team2 = players[match.number_players:]
    else:
        team1 = players[:]
        team2 = None

    context = {'match': match, 'team1': team1, 'team2': team2}
    return render(request, 'base/generate_team.html', context=context)
