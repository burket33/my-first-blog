from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from datetime import datetime
from random import randint

from underdog.models import Pick, Matchup

# task scheduler will run this every day at 1:01 PM
class Command(BaseCommand):

	def handle(self, **options):
		if datetime.today().weekday() == 6: # check if day is Sunday
			set_default_picks()
		

def set_default_picks():
	curr_week = current_week()
	persons = User.objects.all()
	for person in persons:
		person_picks = Pick.objects.filter(person = person)
		week_pick_list = []
		for pick in person_picks:
			week_pick_list.append(pick.matchup.week)
		if not curr_week in week_pick_list:
			def_matchup = default_matchup(curr_week)
			default_pick = Pick(person= person, matchup = def_matchup)
			default_pick.save()
	


def current_week():
	matchups = Matchup.objects.order_by('-week')
	current_week = matchups[0].week
	return current_week
	
def default_matchup(curr_week):
	week_matchups = Matchup.objects.filter(week = curr_week)
	random_number = randint(0, len(week_matchups)-1)
	def_matchup = week_matchups[random_number]
	return def_matchup
	