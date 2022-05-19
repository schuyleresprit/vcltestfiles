import os
import csv
import codecs
import json
from geopy import geocoders
from operator import itemgetter


## TO DO ##
## add State/Province/County information for location data ##


# ---------
# Settings
# ---------

CSV_LOCATION = os.getcwd() + '/raw-data/'
AUTHOR_ID_JSON = os.path.dirname(os.getcwd()) + '/data/test_author_ids.json'
BIBLIOGRAPHIES_JSON = os.path.dirname(os.getcwd()) + '/data/test_bibliographies.json'
INTERSECTIONS_JSON = os.path.dirname(os.getcwd()) + '/data/test_intersections.json'
PLACES_JSON = os.path.dirname(os.getcwd()) + '/data/test_places.json'
COUNTRIES_JSON = os.path.dirname(os.getcwd()) + '/data/test_countries.json'
LANGUAGES_JSON = os.path.dirname(os.getcwd()) + 'data/test_languages.json'
GENRES_JSON = os.path.dirname(os.getcwd()) + 'data/test_genres.json'
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


# -------------------------------------------------------------------------
# Returns a dictionary of author ids (key is the author name and the value is their id)
# author_ids = { 'Aime Cesaire':'acesaire', 'Lydia Cabrera':'lcabrera', ...}
# Returns a dictionary of places
# places = { 'PlaceName': {'Lat': xxx, 'Long': yyy, 'Place ID': ##}, ... }
# Returns a dictionary each author movement
# author_movements =  { 'acesaire': [{'PlaceID':'paris_france', 'StartDate': ''}, {...}, ... ], 'lcabrera': [ {}...] , ... }
# The keys for each movement in the author_movements dictionary are as follows:
# PlaceID, Notes, EntryIndex, StartDate, StartType, StartCitation, EndDate, EndType, EndCitation
#-------------------------------------------------------------------------
def process_scholar_files(csv_path, csv_list, geonames_username):
    author_ids = {}
    author_publications = {}
    Date = {}
    author_country = {}
    pub_places = {}

    for csv_name in csv_list:

        with open(csv_path+csv_name) as csv_file:

            reader = csv.reader(csv_file)

            # get the author information from the csv header
            author_info = reader.__next__()
            author_name = author_info[0]
            author_id = author_info[1]
            author_country = author_info[2]
            author_ids[author_name] = author_id

            #read the rest of the csv to get the author's movements
            author_publications[author_id] = []

            reader = csv.DictReader(csv_file)
            row_index = 0
            for row in reader:
                #if not(row['Pubdate'] == ''):

                    #place_info = row['City'] + ', ' + row['Country']

                    #lat, long = get_lat_long(place_name, geonames_username)
                    #place_info['Lat'] = lat
                    #place_info['Long'] = long

                    #place_id = row['Pub_id']
                    #place_info['Pub_id'] = place_id

                    #pub_places[place_name] = place_info


                    author_publications['Title'] = row['Title']
                    author_publications['Publisher'] = row['Publisher']
                    author_publications['Location'] = row['Pub_id']
                    author_publications['Descriptor'] = row['Descriptor']
                    author_publications['EntryIndex'] = row_index

                    #publication[author_publications] = []
                    author_publications[author_id].append(author_publications)
                    row_index += 1

            csv_file.close()

    return author_ids, author_publications, places


#-------------------------------------------------------------------------
# Returns the earliest and latest dates in the data
#-------------------------------------------------------------------------
def get_earliest_and_latest_dates(author_publications):
    start_dates = []
    end_dates = []

    for author_id in author_publications:
        for movement in author_publications[author_id]:
            start_date = publication['FirstDate']
            end_date = publication['LatestDate']

            if not start_date == '': start_dates.append(start_date)
            if not end_date == '': end_dates.append(end_date)

    start_dates = sorted(start_dates)
    end_dates = sorted(end_dates)

    return start_dates[0], end_dates[len(end_dates)-1]


#-------------------------------------------------------------------------
# Returns a dictionary with keys for every year-month from the earliest
# year in the data to the latest year in the data, for example:
# date_dict = {'1899-01': [], '1899-02': [], ... , '1999-12': []}
#-------------------------------------------------------------------------
def create_date_dict(author_publications):
    date_dict = {}

    earliest_date, latest_date = get_earliest_and_latest_dates(author_publications)

    start_year = int(earliest_date.split('-')[0])
    end_year = int(latest_date.split('-')[0])

    for year in range(start_year, end_year + 1):

            date_dict[year] = []
    return date_dict


#-------------------------------------------------------------------------
# Returns the dictionary for the bibliographies json
#-------------------------------------------------------------------------
def get_bibliographies(author_publications):
    bibliographies = create_date_dict(author_publications)

    for author_id in author_publications:
        for publication in author_publications[author_id]:

            start_date = date_to_year_format(publication['StartDate'])
            end_date = date_to_year_format(publication['EndDate'])

            publication['AuthorID'] = author_id
            if not start_date == '':
                bibliographies[start_date].append(publication)
            if not start_date == end_date and not end_date == '':
                bibliographies[end_date].append(publication)

            # dates_in_place = get_dates_in_place(movement)
            # for date in dates_in_place:
            #     itineraries[date].append(itinerary_output)

    return bibliographies


#-------------------------------------------------------------------------
# Creates the output for the intersections json
# If either the current_place and previous_place provided are of type None
# it does not list the author as in that place for the date range provided
#-------------------------------------------------------------------------
def populate_dates_in_place(from_date, to_date, current_place, current_publication, previous_place, previous_movement, author_id, intersections):
    dates_in_place = get_dates_in_place(from_date, to_date)

    for date in dates_in_place:
        if not current_place == None:
            if not current_place in intersections[date]: intersections[date][current_place] = []
            current_publication['AuthorID'] = author_id
            intersections[date][current_place].append(current_movement)

        if not previous_place == None:
            if not previous_place in intersections[date]: intersections[date][previous_place] = []
            previous_publication['AuthorID'] = author_id
            intersections[date][previous_place].append(previous_movement)

    return intersections


#-------------------------------------------------------------------------
# Processes each movement for the intersections json and assigns likelihood scores for each location.
# These comments are written using Lydia Cabrera as an example.
# Score of 3
# If we have both a start date and an end date for a given location,
# then Cabrera was very likely in that place from that start date through that end date,
# so she appears in that location throughout that date range with a likelihood score of 3.
#
# If we only have a start date or an end date for a given place, then we look at the previous row to help figure out
# Cabrera's likely locations and assign likelihood scores of 2 or 1 for where Cabrera could be, as follows:
#
# Score of 2
# If Cabrera had unterminated time in New York City (meaning an arrival, an earliest presence, or a latest presence),
# and then arrived in Miami, we say she was likely in New York City (with a score of 2) until her arrival in Miami.
# If Cabrera had a departure from Havana followed by an earliest presence, latest presence, or departure from Miami,
# we say she was likely in Miami (with a score of 2) from her Havana departure to her know date in Miami.
#
# Score of 1
# If it is possible that Cabrera could have been in any one of two places,
# then she placed in both locations with a likelihood score of 1 for each.
#-------------------------------------------------------------------------
def process_publication(previous_publication, current_publication, author_id, intersections):
    current_place = current_publication['PubID']

    # current movement has a start date and an end date
    if (not current_publication['StartDate'] == '') and (not current_publication['EndDate'] == ''):
        intersections = populate_dates_in_place(current_publication['StartDate'], current_publication['EndDate'],
                                                current_place, current_publication, None, None, 3, author_id, intersections)

    # current movement has either a start date or an end date
    elif not previous_publication == None: # not the first row in the CSV
        previous_place = previous_publication['PubID']

        # set the from_date and to_date
        if not previous_publication['EndDate'] == '': from_date = previous_publication['EndDate']
        else: from_date = previous_publication['StartDate']

        if not current_publication['EndDate'] == '': to_date = current_publication['EndDate']
        else: to_date = current_publication['StartDate']


    return intersections


#-------------------------------------------------------------------------
# Returns the dictionary for the intersections json
#-------------------------------------------------------------------------
def get_intersections(author_publications):
    intersections = create_date_dict(author_publications)
    for date in intersections: intersections[date] = {}

    for author_id in author_publications:
        # sort movements by EntryIndex
        sorted_by_entry_id = sorted(author_publications[author_id], key=itemgetter('EntryIndex'))

        previous_publication = None
        for current_publication in sorted_by_entry_id:
            intersections = process_publication(previous_publication, current_publication, author_id, intersections)
            previous_publication = current_publication

    # Remove places with no intersections... (where only one person in one place on a given date)
    # for date in list(intersections.keys()):
    #     for place in list(intersections[date].keys()):
    #         if len(intersections[date][place]) == 1:
    #             del intersections[date][place]

    return intersections


# ---------------
# Function calls
# ---------------

csv_list = get_csv_list(CSV_LOCATION)
author_ids, author_publications, pub_places = process_scholar_files(CSV_LOCATION, csv_list, GEONAMES_USERNAME)

publications = get_bibliographies(author_publications)
intersections = get_intersections(author_publications)

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
    f.write(json.dumps(bibliographies, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
    f.close()

with codecs.open(INTERSECTIONS_JSON, 'w', 'utf8') as f:
    f.write(json.dumps(intersections, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
    f.close()



#-------------------------------------------------------------------------
# Unused code (maybe, maybe helpful)
#-------------------------------------------------------------------------

# from operator import itemgetter
# # sort all of the movements by the 'Earliest Known Date' key
# sorted_by_entry_date = sorted(author_movements[author_id], key= itemgetter('Earliest Known Date'))
# author_movements[author_id] = sorted_by_entry_date

# from dateutil import parser
# import datetime
# row['Earliest Year'] = parser.parse(row['Earliest Known Date']).date().year
# row['Earliest Month'] = parser.parse(row['Earliest Known Date']).date().month
# row['Last Year'] = parser.parse(row['Last Known Date']).date().year
# row['Last Month'] = parser.parse(row['Last Known Date']).date().month

# # alternative way to get longitude and latitude information
# from geopy.geocoders import Nominatim
# geolocator = Nominatim()
# location = geolocator.geocode(place_name)
# if location == None:
#     print(place_name, "not found.")
#     return None, None
# else:
#     return location.latitude, location.longitude
