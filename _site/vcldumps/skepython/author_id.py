import csv
import json

def get_author_info():

    with open(author_template.csv, r, encoding = 'utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for line [0] in csv_file:
      # get the author information from the csv header
            author_name = row[0]
            author_id = row[1]
            author_country = row[2]

    return (author_name, author_id, author_country)

def make_json():
    with get_author_info:

        with open(author_info.json, w) as json_file:
            return (author_name, author_id, author_country)
