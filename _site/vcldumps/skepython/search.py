import csv

def searchByLanguage():
    language=str(input('Enter language name to show data\n'));
    csv_file=csv.reader(open('vcltest.csv','r'))


    for row in csv_file:
      if language==row[5]:
          count=row.count
          print(row)
          print(count)

def searchByDate():
    year=str(input('Enter date to show data\n'))
    csv_file=csv.reader(open('vcltest.csv','r'))


    for row in csv_file:
        if year in row[0]:
            count=row.count
            print(row)
            print(count)

def searchByLocation():
    location=str(input('Enter author country to show data\n'));
    csv_file=csv.reader(open('vcltest.csv','r'))


    for row in csv_file:
      if location==row[7]:
          count=row.count
          print(row)
          print(count)

print('Enter 1 to search by language')
print('Enter 2 to search by date')
print('Enter 3 to search by author country')

src=int(input('Enter here: '))

if src==1:
    searchByLanguage()
elif src==2:
    searchByDate()
elif src==3:
    searchByLocation()
else:
    print('Invalid input: sorry')
