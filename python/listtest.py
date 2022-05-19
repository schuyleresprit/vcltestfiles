import os
import csv
import pandas as pd
import datetime
import codecs
import json
import glob
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

	print(csv_list)
