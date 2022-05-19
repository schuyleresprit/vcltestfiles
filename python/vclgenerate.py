import os
import csv
import pandas as pd
import datetime
import codecs
import json
from geopy import geocoders
from operator import itemgetter

# ---------
# Settings
# ---------

CSV_LOCATION = os.getcwd() + '/raw-data/'
AUTHOR_ID_JSON = os.path.dirname(os.getcwd()) + '/data/author_ids.json'
BIBLIOGRAPHIES_JSON = os.path.dirname(os.getcwd()) + '/data/bibliographies.json'
INTERSECTIONS_JSON = os.path.dirname(os.getcwd()) + '/data/intersections.json'
PLACES_JSON = os.path.dirname(os.getcwd()) + '/data/places.json'
COUNTRIES_JSON = os.path.dirname(os.getcwd()) + '/data/countries.json'
LANGUAGES_JSON = os.path.dirname(os.getcwd()) + '/data/languages.json'
GENRES_JSON = os.path.dirname(os.getcwd()) + '/data/genres.json'
TRANSLATIONS_JSON = os.path.dirname(os.getcwd()) + '/data/translations.json'
GEONAMES_USERNAME = 'schuylere'

# ----------
# Functions
# ----------

#-------------------------------------------------------------------------
# Returns a list of all the csv files in a directory
#-------------------------------------------------------------------------
def get_csv_list(csv_location):
	csv_list = []

	file_list = os.listdir(csv_location)
	for file in file_list:
		if file.lower().endswith('.csv'): csv_list.append(file)

	return csv_list

#-------------------------------------------------------------------------
# Returns the GeoNames latitude and longitude of the place name provided.
# If the place is not found, the function returns None for both longitude and latitude.
#-------------------------------------------------------------------------
def get_lat_long(place_name, geonames_username):
	gn = geocoders.GeoNames(username=geonames_username, timeout=None)
	location = gn.geocode(place_name,timeout=None)
	if location == None:
		print(place_name, "not found.")
		return None, None
	else:
		return location.latitude, location.longitude
#--------------------------------------------------------------------------
def get_author_country_geo(author_country, geonames_username):
	gn = geocoders.GeoNames(username=geonames_username, timeout=None)
	location = gn.geocode(author_country,timeout=None)
	if location == None:
		print(author_country, "not found.")
		return None, None
	else:
		return location.latitude, location.longitude
# -------------------------------------------------------------------------
# Returns a dictionary of author ids (key is the author name and the value is their id)
# Returns a dictionary of places
# places = { 'PlaceName': {'Lat': xxx, 'Long': yyy, 'Pub_id': ##}, ... }
# Returns a dictionary each author movement# The keys for each movement in the author_movements dictionary are as follows:
#-------------------------------------------------------------------------
def process_author_files(csv_path, csv_list, geonames_username):
	author_ids = {}
	publications = {}
	author_publications = {}
	translations = {}
	places = {}
	countries = {}
	#languages = {}
	#genres = {}

	for csv_name in csv_list:
		with open(csv_path+csv_name) as csv_file:
			reader = csv.reader(csv_file)

#------------------------------------------------
# get the author information from the csv header
#------------------------------------------------
			author_info = reader.__next__()
			author_name = author_info[0]
			author_id = author_info[1]
			author_country = author_info[2]
			author_ids[author_name] = author_id
			#publications[author_id] = []

#----------------------------------------------------------------
#get author country coordinates for each author_id
#----------------------------------------------------------------
			lat, long = get_author_country_geo(author_country, geonames_username)

			country_name = author_info[2]
			#author_country = author_info[2]
			if not country_name in countries:
				country_info = {}
				country_info['Lat'] = lat
				country_info['Long'] = long
				country_id = author_info[2]
				#country_id = country_info['author_country']

				country_info['author_country'] = country_id
				countries[country_name] = country_info



#--------------------------------------------------------------------
#get Pub_id coordinates for each Pub_id
#-------------------------------------------------------------------
	for csv_name in csv_list:
		with open(csv_path+csv_name) as csv_file:
			reader = csv.reader(csv_file)
			place_info = reader.__next__()

			row_index = 2

			for row in reader:
				place_name = row[5] + ', ' + row[6]

				if not place_name in places:
					place_info = {}

					lat, long = get_lat_long(place_name, geonames_username)
					place_info['Lat'] = lat
					place_info['Long'] = long

					place_id = row[7]
					place_info['Pub_id'] = place_id

					places[place_name] = place_info

#----------------------------------------------------------
#read the rest of each csv to get the author's publications
#----------------------------------------------------------
	for csv_name in csv_list:
		with open(csv_path+csv_name) as csv_file:
			reader = csv.reader(csv_file)
			#reader = csv.DictReader(csv_file)

			#row2 = next(reader)
			#author_publications = reader.__next__()

			row_index = 2
			for row in reader:
				#print(row)

				author_publications = {}
				author_publications['Author'] = row[0]
				author_publications['Title'] = row[1]
				author_publications['Pubdate'] = row[2]
				author_publications['Language'] = row[3]
				author_publications['Publisher'] = row[4]
				author_publications['Pub_id'] = places[place_name]['Pub_id']
				author_publications['Genre'] = row[8]
				author_publications['Translation'] = row[9]
				author_publications['Descriptor'] =  row[11]
				author_publications['EntryIndex'] = row[row_index]

				#publications[author_id].append(author_publications)
				row_index += 1

				#title = author_publications['Title']

				#language_id = author_publications['Language']
				#languages = language_id

				#genre_id = author_publications['Genre']
				#genres = author_id + title + genre_id

		print(author_ids)
		print(author_publications)
		csv_file.close()


	return author_ids, author_publications, places, countries#, languages, genres

#------------------------------------------------------------------------------
#get language data
#for each author_id return a list of each title and corresponding language
#------------------------------------------------------------------------------
def get_languages(author_ids, author_publications):
	language_id = author_publications['Language']
	languages = author_publications[language_id]
	title = author_publications['Title']

	for title in author_publications[author_ids]:
	#for title in author_publications:

		return languages

#-------------------------------------------------------------------------
# Takes a string date and returns the year version of that date
#-------------------------------------------------------------------------
def make_year(date):
	pd.to_datetime(author_publications['Pubdate'])
	return date

#-------------------------------------------------------------------------
# Returns the dictionary for the bibliographies json
#for each author, return a list of all titles and dates
#------------------------------------------------------------------------
def get_bibliographies(author_ids, author_publications):
	publisher = author_publications['Publisher']
	pubdate = author_publications['Pubdate']
	date = make_year(pubdate)
	book = author_publications['Title']
	bibliographies = (book, date, publisher)
	print(author_ids)
	print(author_publications)
	for author_ids in author_publications:

	#for author_id in author_publications:

		return bibliographies

#---------------------------------------------------------------------------
#get the translated titls from the llst by author_id
#---------------------------------------------------------------------------
def get_translations(author_ids, author_publications):
	translation = set(author_publications['Translation'])
	title = set(author_publications['Title'])
	for title in author_publications:
		if author_publications['Translation'] == 'y':

			return translation
#(glob.glob(''*.csv')):
# ---------------
# Function calls
# ---------------
csv_list = get_csv_list(CSV_LOCATION)
author_ids, author_publications, places, countries = process_author_files(CSV_LOCATION, csv_list, GEONAMES_USERNAME)
#languages, genres
publications = get_bibliographies(author_ids, author_publications)
translations = get_translations(author_ids, author_publications)

with codecs.open(AUTHOR_ID_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(author_ids, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()

with codecs.open(COUNTRIES_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(countries, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()

with codecs.open(PLACES_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(places, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()

with codecs.open(LANGUAGES_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(languages, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()

with codecs.open(GENRES_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(genres, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()

with codecs.open(BIBLIOGRAPHIES_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(publications, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()

with codecs.open(TRANSLATIONS_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(translations, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()
