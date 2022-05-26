#-------------------------------------------------------------------------
# Takes a string date and returns the year version of that date
#-------------------------------------------------------------------------
def make_year(date):
	author_publications = {}
	pd.to_datetime(author_publications['Pubdate'])
	return date
#---------------------------------------------------------------------------
def create_date_dict(author_publications):
	date = {}
	#row_index = 1
	#for row in reader:
	pubdate = make_year(date)
	#earliest_date, latest_date = get_earliest_and_latest_dates(author_publications)
	start_year = (1800)
	end_year = (2022)

	for year in range(start_year, end_year + 1):
	#date_dict[year] = []
		return date_dict

def get_timeline(author_publications, places):
	#date = make_year(date)
	date_dict = create_date_dict(publications)
	pubdate = row['Pubdate']
	date = make_year(pubdate)
	book = row['Title']
	place = row['Pub_id']
	publisher = row['Publisher']
	for date in date_dict:
		author_publications[author_id].append(book, place, publisher)
		return timeline
#-------------------------------------------------------------------------
# Returns the dictionary for the bibliographies json
#for each author, return a list of all titles and dates
#------------------------------------------------------------------------
#def get_bibliographies(author_ids, author_publications):
	#publisher = row['Publisher']
	#pubdate = row['Pubdate']
	#date = make_year(pubdate)
	#book = row['Title']
	#bibliographies = (book, date, publisher)

	#print(author_publications)
	#for author_ids in publications:

	#for author_id in author_publications:

		#return bibliographies


        #for row in reader:
            #languages = author_publications['Language']




		for csv_name in csv_list:
			with open(csv_path+csv_name) as csv_file:
				reader = csv.reader(csv_file)

				#for row in reader:

				lang = {}
				language_id = reader.__next__()
				lang['English'] = ['English']
				lang['French'] = ['French']
				lang['Spanish'] = ['Spanish']
				lang['Haitian Creole'] = ['Haitian Creole']
				lang['Czech'] = ['Czech']
				language_id = []
				languages = {(row['Language'],[]) for language_id in publications}
				#for language_id in range(author_publications):
				print (languages)

				#for language_id, (lang, language_id) in enumerate(publications.items()):
					#languages = (lang, language_id)
				#if language_id in publications and languages == languages[language_id]:
				#for language_id in languages:
					#language_id.append(publications)
					#filter(publications, languages)
				#languages[language_id].append(publications)


				#row = reader.__next__()


				#------------------------------------------------------------------------------
				#Create a dictionary for the Genres
				#------------------------------------------------------------------------------
					for csv_name in csv_list:
						with open(csv_path+csv_name) as csv_file:
							reader = csv.reader(csv_file)

							#for row in reader:

							genres = author_publications['Genre']
							genre_id = reader.__next__()

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
							genre_id = []
								#genre_id == ['']
								#author_publications['Genre'] = genre_id

							for genre_id in genres:
								#if genre_id in genres:
								#genres[genre_id] = []
								genres[genre_id].append(publications)

					for csv_name in csv_list:
						with open(csv_path+csv_name) as csv_file:
							reader = csv.reader(csv_file)

							#for row in reader:
							translations = author_publications['Translation']
							translation_id = reader.__next__()
							translations = {}
								#author_publications['Translation'] = ['Translation']
							translations['y'] = ['y']
							translations['n'] = ['n']
								#translations_y = translations['y']
							translation_id = []
								#translation = set(author_publications['Translation'])
								#title = [publication_id]
							for translation_id in translations:
								#if [translation_id] == ['y']:
								translations[translation_id].append(publications)

            #author_publications['Language'] = language_id
            #languages[language_id] = []
            #if language_id in languages:
