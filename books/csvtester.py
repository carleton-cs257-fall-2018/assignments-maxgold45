import csv

unix_dialect = csv.get_dialect("unix")
with open("books.csv", newline='') as csvfile:
    book_reader = csv.reader(csvfile, dialect="unix")
    for entry in book_reader:
        print(entry[0])

