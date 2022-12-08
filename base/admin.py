from django.contrib import admin
from . import models


# Register your models here.


class MatchAdmin(admin.ModelAdmin):
    fields = ['match_name']


admin.site.register(models.Player)
admin.site.register(models.Match, MatchAdmin)
