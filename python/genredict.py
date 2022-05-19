import os
import csv
import pandas as pd
import datetime
import codecs
import json
from geopy import geocoders
from operator import itemgetter

CSV_LOCATION = os.getcwd() + '/raw-data/'
GENRES_JSON = os.path.dirname(os.getcwd()) + '/data/genres.json'

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

def get_genre(csvfile):
	genres = {}

	for csv_name in csv_list:
		with open(CSV_LOCATION+csv_name) as csvfile:
			reader = csv.DictReader(csvfile)
	for row in reader:
		title_col = {'Title': []}
		genre_col = {'Genre': []}
		genre = record['Genre']

	for record in reader:
			genre_col['Genre'].append(record['Genre'])



	csv_list = get_csv_list(CSV_LOCATION)
	#genres = get_genre(csv_list)
	#return genre
with codecs.open(GENRES_JSON, 'w', 'utf8') as f:
	f.write(json.dumps(genres, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
	f.close()
