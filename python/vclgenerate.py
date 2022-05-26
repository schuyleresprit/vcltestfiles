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
AUTHOR_PUBLICATIONS_JSON = os.path.dirname(os.getcwd()) + '/data/author_publications.json'
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
	#timeline = {}
	translations = {}
	places = {}
	countries = {}
	languages = {}
	genres = {}

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
			publications[author_id] = []
			#languages[language_id] = []
			#genres[genre_id] = []

#----------------------------------------------------------------
#get author country coordinates for each author_id
#----------------------------------------------------------------
			lat, long = get_author_country_geo(author_country, geonames_username)

			country_name = author_info[2]
			if not country_name in countries:
				country_info = {}
				country_info['Lat'] = lat
				country_info['Long'] = long
				country_id = author_info[2]
				country_info['author_country'] = country_id
				countries[country_name] = country_info

#--------------------------------------------------------------------
#get Pub_id coordinates for each Pub_id
#-------------------------------------------------------------------

			reader = csv.DictReader(csv_file)
			row_index = 0
			for row in reader:
				if not(row['Title'] == '' and row['Pubdate'] == '' and row['Language'] == '' and row['Genre'] == ''):
					place_name = row['Pub_city'] + ', ' + row['Pub_country']

				if not place_name in places:
					place_info = {}

					lat, long = get_lat_long(place_name, geonames_username)
					place_info['Lat'] = lat
					place_info['Long'] = long

					place_id = row['Pub_id']
					place_info['Pub_id'] = place_id

					places[place_name] = place_info

#----------------------------------------------------------
#read the rest of each csv to get the author's publications
#----------------------------------------------------------
				author_publications = {}
				author_publications ['Author'] = author_info[0]
				author_publications['Pub_id'] = places[place_name]['Pub_id']
				author_publications['Title'] = row['Title']
				author_publications['Pubdate'] = row['Pubdate']
				author_publications['Language'] = row['Language']
				author_publications['Publisher'] = row['Publisher']
				author_publications['Genre'] = row['Genre']
				author_publications['Translation'] = row['Translation']
				author_publications['Descriptor'] =  row['Descriptor']

				publication_id = row['Title']
				author_publications['Title'] = publication_id
				language_id = row['Language']
				author_publications['Language'] = language_id
				genre_id = row['Genre']
				author_publications['Genre'] = genre_id
				translation_id = row['Translation']
				author_publications['Translation'] = translation_id
				date_id = row['Pubdate']
				author_publications['Pubdate'] = date_id
				publications[author_id].append(author_publications)


#--------------------------------------------------------------------------------
#Create a dictionary for the LANGUAGES
#-------------------------------------------------------------------------------
	for csv_name in csv_list:
		with open(csv_path+csv_name) as csv_file:
			reader = csv.reader(csv_file)
			row_index = 3

			for row in reader:

				#language_id = reader.__next__()
				languages = {}
				languages['English'] = ['English']
				languages['French'] = ['French']
				languages['Spanish'] = ['Spanish']
				languages['Haitian Creole'] = ['Haitian Creole']
				languages['Czech'] = ['Czech']
				#language_id = []
				print(languages )
				#for language_id in languages:
				#for language_id in languages:
					#if language_id == True:
						#filter(publications)
				languages[language_id].append(author_publications)
				print(languages)

#------------------------------------------------------------------------------
#Create a dictionary for the Genres
#------------------------------------------------------------------------------
	for csv_name in csv_list:
		with open(csv_path+csv_name) as csv_file:
			reader = csv.reader(csv_file)

			for row in reader:

				#genres = author_publications['Genre']
			#genre_id = reader.__next__()

				genres = {}
				genres['Fiction (Novel)'] = ['Fiction (Novel)']
				genres['Fiction (Novella)'] = ['Fiction (Novella)']
				genres['Fiction (Short Story Collection)'] = ['Fiction (Short Story Collection)']
				genres['Drama'] = ['Drama']
				genres['Poetry Collection'] = ['Poetry Collection']
				genres['Short Story'] = ['Short Story']
				genres['Poem'] = ['Poem']
				genres['Nonfiction Book'] = ['Nonfiction Book']
				genres['Biography'] = ['Biography']
				genres['Autobiography/Memoir'] = ['Autobiography/Memoir']
				genres['Anthology'] = ['Anthology']
				genres[''] = ['NA']
				#genre_id = []
				#genre_id == ['']
				#author_publications['Genre'] = genre_id

				#for genre_id in genres:
				#if genre_id in genres:
				#genres[genre_id] = []
				genres[genre_id].append(author_publications)

			csv_file.close()

		return author_ids, publications, places, countries, languages, genres

#---------------------------------------------------------------------------
#get the translated title from the llst by author_id
#---------------------------------------------------------------------------
def get_translations(publications):
	for author_id in publications:
		#author_publications ={}
		#for author_publications['Translation'] in author_publications:
		#author_publications = {}
		#author_publications['Translation'] = ['Translation']
			#translation = author_publications['Translation']
		#publication_id = ['Title']
		#title = [publication_id]
			#for translation in author_publications:
				if ['Translation'] == 'y':
					return translation

# ---------------
# Function calls
# ---------------
csv_list = get_csv_list(CSV_LOCATION)
author_ids, publications, places, countries,languages, genres = process_author_files(CSV_LOCATION, csv_list, GEONAMES_USERNAME)

#timeline = get_timeline(publications, places)
#languages = get_languages(author_ids, publications)
#genres = get_genres(author_ids, publications)
translations = get_translations(publications)

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

#with codecs.open(BIBLIOGRAPHIES_JSON, 'w', 'utf8') as f:
	#f.write(json.dumps(timeline, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	#f.close()

with codecs.open(AUTHOR_PUBLICATIONS_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(publications, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()

with codecs.open(TRANSLATIONS_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(translations, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()
