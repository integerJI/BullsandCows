from django.contrib import admin
from .models import GameRomm, GameNum, GameTryNum

# Register your models here.
admin.site.register(GameRomm)
admin.site.register(GameNum)
admin.site.register(GameTryNum)