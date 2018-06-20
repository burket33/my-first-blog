from django.core.management.base import BaseCommand

from datetime import datetime

from bs4 import BeautifulSoup

from underdog.models import NFLTeam, Matchup

class Command(BaseCommand):

	def add_arguments(self, parser):
		parser.add_argument('html_filestring')
		parser.add_argument('week')
	
	def handle(self, *args, **options):
		html_filestring = options['html_filestring']
		week = options['week']
		import_matchups(html_filestring, week)

def import_matchups(html_filestring, week):

	html_doc = html_filestring

	soup = BeautifulSoup(open(html_doc), 'html.parser')

	temp_list= []
	count = 1


	for data in soup.find_all('td'):
		if count < 7:
			temp_list.append(data.text.upper())
			count += 1
		else:
			temp_list.append(data.text.upper())
			index_count = 0
			for item in temp_list:
				if item[0:3] == 'AT ':
					temp_list[index_count] = item[3:]
					temp_list.append(item[3:])
					home_team_name = item[3:]
				index_count += 1
			favorite = NFLTeam.objects.get(name = temp_list[1])
			underdog = NFLTeam.objects.get(name = temp_list[3])
			if home_team_name == favorite.name:
				home_team = 'FAV_TEAM'
			elif home_team_name == underdog.name:
				home_team = 'UNDER_TEAM'
			spread = temp_list[2]
			game_time = datetime.strptime(temp_list[0], '%B %d, %Y %I:%M %p')
			m = Matchup(favorite = favorite, underdog = underdog, home_team = home_team, spread = spread, week = week, game_time = game_time)
			m.save()
			temp_list = []
			count = 1
