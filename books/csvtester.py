import csv

input_file = input("Input file? ")
sort_direction = input("Sort direction? 'reverse', 'forward', or empty (defaults to forward) ")
action = input("Action? 'books' or 'authors' ")

#these inputs would normally come from the command line, using normal python input for now
#also needs error checking and failure statement as described in instructions

unix_dialect = csv.get_dialect("unix")
with open(input_file, newline='') as csvfile:
    book_reader = csv.reader(csvfile, dialect="unix")
    if action == "books":
        title_list = []
        for entry in book_reader:
            title_list.append(entry[0])
        title_list.sort()
        if sort_direction == "reverse":
            title_list.reverse()        
        for title in title_list:
            print(title)
    elif action == 'authors':
        pass
    else:
        print("you didn't write 'books' or 'authors'!")
