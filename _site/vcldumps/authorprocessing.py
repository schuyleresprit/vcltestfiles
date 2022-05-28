import csv

def process_author_files():
    vcltest = (r'rantoni.csv')
    with open (vcltest, encoding = 'utf')as csvfile:
        reader = csv.DictReader(csvfile)
        row_index = 0
        for row in reader:
# get the author information from the csv header
            author_info = reader.__next__()
            author_name = author_info[0]
            author_id = author_info[1]
            author_country = author_info[2]
            author_ids[author_name] = author_id


#read the rest of the csv to get the author's publications
            author_publications[author_id] = []



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

    csvfile.close()

    print(author_id)
