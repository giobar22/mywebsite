from django.contrib import admin
from . models import *

class GameNewsAdmin(admin.ModelAdmin):
    list_display = ['title','developer','year_of_issue']
    search_fields = ['title']

admin.site.register(GameNews,GameNewsAdmin)
admin.site.register(Genre)
admin.site.register(UpComingGames)


