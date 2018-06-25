from django.contrib import admin

from .models import NFLTeam, Matchup, Pick, GameResult

class PickAdmin(admin.ModelAdmin):
	readonly_fields = ('created_at', 'updated_at',)
	
class NFLTeamAdmin(admin.ModelAdmin):
	list_display = ('city', 'name')
	
class MatchupAdmin(admin.ModelAdmin):
	list_display = ('favorite', 'underdog', 'week')
	list_filter = ('week',)
	
class PickAdmin(admin.ModelAdmin):
	list_display = ('person', 'matchup', 'week')
	list_filter = ('matchup__week',)
	
class GameResultAdmin(admin.ModelAdmin):
	list_display = ('matchup', 'points_for_pick')
	list_filter = ('matchup__week',)

admin.site.register(NFLTeam, NFLTeamAdmin)

admin.site.register(Matchup, MatchupAdmin)

admin.site.register(Pick, PickAdmin)

admin.site.register(GameResult, GameResultAdmin)

