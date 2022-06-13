from django.contrib import admin
from .models import *


class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'years_old', 'time_create', 'moves')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('sex', 'time_create')


# class MovesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'moves')
#     list_display_links = ('id', 'name')
#     search_fields = ('moves',)


admin.site.register(Players, PlayersAdmin)
# admin.site.register(Moves, MovesAdmin)
