import csv
import xml.etree.ElementTree as ET
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from underdog.models import NFLTeam, Matchup, GameResult

def import_game_results(xml_filestring, week):
	xml_doc = xml_filestring
	
	tree = ET.parse(xml_doc)
	root = tree.getroot()
	
	# filter matchups for specific week
	qs_matchups = Matchup.objects.filter(week = week)

	
	for child in root:
		for node in child:
			xml_dict = node.attrib
			home_team = NFLTeam.objects.get(name = xml_dict['hnn'].upper())
			away_team = NFLTeam.objects.get(name = xml_dict['vnn'].upper())
			try:
				matchup = qs_matchups.get(favorite = home_team)
			except ObjectDoesNotExist:
				matchup = qs_matchups.get(favorite = away_team)
			if matchup.favorite == home_team:
				fav_score = int(xml_dict['hs'])
				under_score = int(xml_dict['vs'])
			else:
				fav_score = int(xml_dict['vs'])
				under_score = int(xml_dict['hs'])
			if fav_score > under_score:
				winner = 'FAV_TEAM'
				points_for_pick = -1 * ((fav_score - under_score) // 10)
			elif under_score > fav_score:
				winner = 'UNDER_TEAM'
				points_for_pick = -1 * matchup.spread 
			else:
				points_for_pick = 0
			game_result = GameResult(matchup = matchup, winner = winner, favorite_score = fav_score, underdog_score = under_score, points_for_pick = points_for_pick)
			game_result.save()
	
	return xml_dict


	
