import xml.etree.ElementTree as ET

from underdog.models import NFLTeam

def import_NFL_Teams(xml_filestring):
	xml_doc = xml_filestring
	
	tree = ET.parse(xml_doc)
	root = tree.getroot()
	
	for child in root:
		for node in child:
			xml_dict = node.attrib
			home_name = xml_dict['hnn'].upper()
			home_city = xml_dict['h'].upper()
			home_team = NFLTeam(name = home_name, city = home_city)
			home_team.save()
			
			away_name = xml_dict['vnn'].upper()
			away_city = xml_dict['v'].upper()
			away_team = NFLTeam(name = away_name, city = away_city)
			away_team.save()
	
	return xml_dict


	
