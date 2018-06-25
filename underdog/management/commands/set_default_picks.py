from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from datetime import datetime
from random import randint

from underdog.models import Pick, Matchup

# task scheduler will run this every day at 1:01 PM
class Command(BaseCommand):

	def handle(self, **options):
		if datetime.today().weekday() == 6: # check if day is Sunday (6 = sunday, 0 = Monday)
			set_default_picks()
		

def set_default_picks():
	curr_week = current_week()
	persons = User.objects.all()
	week_picks = Pick.objects.filter(matchup__week = curr_week)
	person_with_pick = list_person_with_pick(curr_week)
	for person in persons:
		if not person in person_with_pick:
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
	
def list_person_with_pick(curr_week):
	week_picks = Pick.objects.filter(matchup__week = curr_week)
	person_with_pick = []
	for pick in week_picks:
		person_with_pick.append(pick.person)
	return person_with_pick
	
	