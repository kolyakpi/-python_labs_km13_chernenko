import csv

with open('RAMMSTEIN.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer = csv.DictWriter(csvfile, fieldnames=['Composition', 'year'])
    writer.writeheader()
    writer.writerow({'Composition': 'Sonne',
                     'year': '1998'})
    writer.writerow({'Composition': 'Deutschland',
                     'year': '2003'})
    writer.writerow({'Composition': 'Mein Herz Brennt',
                     'year': '2001'})
    writer.writerow({'Composition': 'Haifisch',
                     'year': '1993'})
    writer.writerow({'Composition': 'Rosenrot',
                     'year': '1996'})
    writer.writerow({'Composition': 'Amerika',
                     'year': '1997'})
    
with open('RAMMSTEIN.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print("\n")
    for row in reader:
        print(row['Composition'], row['year'])