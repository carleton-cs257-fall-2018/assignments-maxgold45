#!!! note: current issues:
#does not sort by last name (use sort key = with a custom function getLastNameFirstLetter)
#does not get rid of 'and' before Terry Pratchett's name (need to do that manually)
#will cause error if file does not exist
#If the command-line syntax is incorrect, your program should print a usage statement that briefly describes the correct command-line syntax. print to stderr

import csv
import sys
import os.path

input_file = sys.argv[1]
action = sys.argv[2]
#if there is a sort direction:
if len(sys.argv) == 4:
        sort_direction = sys.argv[3]
else:
        sort_direction = "forward"

issue = False
# check for errors among inputs:
if not (os.path.isfile(input_file)):
	issue = True
elif not ((action == 'books') or (action == 'authors')):
	issue = True
elif not ((sort_direction == 'forward') or (sort_direction == 'reverse')):
	issue = True

if issue == True:
	print("Incorrect Usage: python3 books1.py input-file action [sort-direction]\ninput-file = the file you wild like to read\naction = \"books\" or authors\"\n[sort-direction] = reverse or forward.", file=sys.stderr)

	sys.exit(1)

#sets the dialect to unix, dialect is just rules for separating entries 
unix_dialect = csv.get_dialect("unix")
#with statement means we don't have to use .close? I think
with open(input_file, newline='', encoding='UTF-8') as csvfile:
    #book_reader is our iterable over the books.csv file
    book_reader = csv.reader(csvfile, dialect="unix")
    
    #'books' code:
    if action == "books":
        title_list = []
        for entry in book_reader: #for each title, add it to the list
            title_list.append(entry[0])
        title_list.sort() #sort the list
        if sort_direction == "reverse": #if the list needs to be reversed, do so
            title_list.reverse()        
        for title in title_list: #print each title
            print(title)

    #'authors' code:
    elif action == 'authors': 
        author_list = []
        for entry in book_reader: #for each string of author/s (could be multiple):
            new_names = entry[2].split(")") #split it up by close parens
            for name in new_names: #for each of the split up names:
                name = name.split("(")[0] #get rid of the date
                name = name.strip() #get rid of whitespace
                if name != "": #if the name isn't blank
                    if name not in author_list: #and it's not already in the list
                        author_list.append(name) #add it to the list

        author_list.sort() #sorts the list
        if sort_direction == "reverse": #if it needs to be reversed
            author_list.reverse() #reverse it
        for author in author_list: #print the authors
            print(author)

    else: #fail statement (should be better)
        print("you didn't write 'books' or 'authors'!")
