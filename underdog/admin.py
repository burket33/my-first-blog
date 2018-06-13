from django.contrib import admin

from .models import NFLTeam, Matchup, Pick, GameResult

class PickAdmin(admin.ModelAdmin):
	readonly_fields = ('created_at', 'updated_at',)

admin.site.register(NFLTeam)

admin.site.register(Matchup)

admin.site.register(Pick, PickAdmin)

admin.site.register(GameResult)

