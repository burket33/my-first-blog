from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#NFL teams Model
class NFLTeam(models.Model):
	name = models.CharField(max_length = 50)
	city = models.CharField(max_length = 3)
	
	def __str__(self):
		return self.name
		
class Matchup(models.Model):
	HOME_TEAM_CHOICES = (('FAV_TEAM', 'Favorite'), ('UNDER_TEAM', 'Underdog'))
	
	favorite = models.ForeignKey(NFLTeam, related_name='fav', on_delete=models.CASCADE)
	underdog = models.ForeignKey(NFLTeam, related_name='under', on_delete= models.CASCADE)
	home_team = models.CharField(max_length= 15, choices = HOME_TEAM_CHOICES, default = 'FAV_TEAM')
	spread = models.FloatField()
	week = models.IntegerField()
	game_time = models.DateTimeField()
	
	def __str__(self):
		matchup = self.favorite.name + ' vs ' + self.underdog.name
		return matchup
		
		
class Pick(models.Model):
	person = models.ForeignKey(User, on_delete = models.CASCADE)
	matchup = models.ForeignKey(Matchup, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		pick_display = str(self.person) + ' ' + str(self.matchup)
		return pick_display
		
class GameResult(models.Model):
	HOME_TEAM_CHOICES = (('FAV_TEAM', 'Favorite'), ('UNDER_TEAM', 'Underdog'))
	
	matchup = models.ForeignKey(Matchup, on_delete=models.CASCADE)
	winner = models.CharField(max_length  = 15, choices = HOME_TEAM_CHOICES, default = 'FAV_TEAM')
	favorite_score = models.IntegerField()
	underdog_score = models.IntegerField()
	points_for_pick = models.FloatField()
	
	def __str__(self):
		result_display = str(self.matchup.favorite) + ' ' + str(self.favorite_score) + ' ' + str(self.matchup.underdog) + ' ' + str(self.underdog_score)
		return result_display