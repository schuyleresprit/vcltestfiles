import csv

with open('vcltest.csv') as f:
    reader = csv.reader(f)
    with open('vclpubplaces.csv', 'w') as g:
        writer = csv.writer(g)
        for row in reader:
            new_row = [', '.join([row[9], row[10]])]
            writer.writerow(new_row)
