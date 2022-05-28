#-------------------------------------------------------------------------
# Returns the earliest and latest dates in the data
#-------------------------------------------------------------------------

def get_earliest_and_latest_dates(author_publications):
	#datetime.strftime(date_string, ('%Y'))

	for author_id in author_publications:
		for publication in author_publications[author_id]:
			start_date = []
			end_date = []

			#if not start_date == '': start_dates.append(start_date)
			#if not end_date == '': end_dates.append(end_date)

	start_dates = sorted(start_dates)
	end_dates = sorted(end_dates)

	return start_dates[0], end_dates[len(end_dates)-1]

    #publication(year) == []
#start_date = []
#end_date = []
if not start_date == '':
    bibliographies[start_date].append(publication)
if not start_date == end_date and not end_date == '':
    bibliographies[end_date].append(publication)


    			# dates_in_place = get_dates_in_place(publication)
    			# for date in dates_in_place:
    			#     bibliographies[date].append(bibliography_output)


                #-------------------------------------------------------------------------
                # Returns the dictionary for the intersections json
                #-------------------------------------------------------------------------
                def get_intersections(author_publications):
                	intersections = author_publications['Pubdate']
                	#for date in intersections: intersections[date] = {}

                	for author_id in author_publications:
                		# sort publications by EntryIndex
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

					#------------------------------------------------------------------------------
					#create date dictionary
					#------------------------------------------------------------------------------
					def create_date_dict(author_publications):
						date_dict = {author_publications['Pubdate']}


						#earliest_date, latest_date = get_earliest_and_latest_dates(author_publications)

						start_year = (1800)
						end_year = (2022)

						for year in range(start_year, end_year + 1):

							#date_dict[year] = []

							return date_dict
	#start_date = make_year([])
	#end_date = make_year([])

for year in author_publications:
	start_date = str(1800)
	end_date = str(2022)
		#year = (author_publications['Pubdate'])

	#lat, long = get_lat_long(place_name, geonames_username)

	#df = pd.DataFrame(lat, long)
	#df['Lat'] = lat
	#df = pd.DataFrame(lat, long)
	#df['Long'] = long



	#countries[author_country] = country_info

	#row_index = 0

	#for row in reader:

	#author_ids[author_name] = author_id

				#author_country = author_info[2]
#next(csv.reader(csv_file))
#row_index = 1

	for csv_name in csv_list:
		with open(csv_path+csv_name) as csv_file:
			reader = csv.reader(csv_file)
			row_index = 1

			for row in reader:


				publication = {}
				publication['Author'] = row[0]
				publication
				publication['Publisher'] = row[4]

						if not author_publications['Author'] == '':
							author_publications['Title'] == ''
							author_publications['Pubdate'] == ''
							author_publications['Publisher'] == ''
							author_publications['Pub_id'] == ''

						else:
							author_publications['Author'] == ''
							author_publications['Title'] == ''
							author_publications['City'] == ''
							author_publications['Country'] == ''
				publication['Pub_id'] = places[place_name]['Pub_id']
				publication['Descriptor'] = row[10]
				publication['EntryIndex'] = row_index



				#author_publications(author_id).append(author_publications)
					#row_index += 1

#lat, long = get_lat_long(place_name, geonames_username)

#df = pd.DataFrame(lat, long)
#df['Lat'] = lat
#df = pd.DataFrame(lat, long)
#df['Long'] = long


	#return places, countries


	#publications = get_bibliographies(author_ids, author_publications)
	#intersections = get_intersections(author_publications)

		#for csv_name in csv_list:
			#with open(csv_path+csv_name) as csv_file:
				#reader = csv.reader(csv_file)
				#reader = csv.DictReader(csv_file)


				#author_publications = reader.__next__()

				#row_index = 0
				#for row in reader:

#for csv_name in csv_list:
	#with open(csv_path+csv_name) as csv_file:
		#reader = csv.reader(csv_file)


#------------------------------------------------------------------------------
#get language data
#for each author_id return a list of each title and corresponding language
#------------------------------------------------------------------------------
#def get_languages(author_ids, author_publications):
	#language_id = author_publications['Language']
	#languages = author_publications[language_id]
	#title = author_publications['Title']

	#for title in author_publications[author_ids]:
	#for title in author_publications:

		#return languages
