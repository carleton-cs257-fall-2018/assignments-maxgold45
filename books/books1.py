#!!! note: current issues:
#Sorts accented 'a' after other letters, when it should probably come before?
#^Above could be fixed by having the get_last_name function replace
# special characters with their normal counterparts.
#does not get rid of 'and' before Terry Pratchett's name (need to do that manually)

import csv
import sys
import os.path

def get_last_name(name_string):
        '''Returns the final word of a string,
        with words being separated by spaces,
        followed by the rest of the name (for tie-breaking).
        '''
        final_space = name_string.rfind(' ')
        return (name_string[final_space+1:]+name_string[:final_space+1])

issue = False 

input_file=""
action=""
sort_direction=""
#Error checks to make sure there are 3 or 4 command ine inputs
if len(sys.argv) == 3 or len(sys.argv) == 4:
        input_file = sys.argv[1]
        action = sys.argv[2]
        #if there is a sort direction:
        if len(sys.argv) == 4:
                sort_direction = sys.argv[3]
        else:
                sort_direction = "forward"

        # check for errors among inputs: (3 ifs so it'll print each issue)
        if not (os.path.isfile(input_file)):
                print ("Your filename (arg1) is incorrect", file=sys.stderr)
                issue = True
        if not ((action == 'books') or (action == 'authors')):
                print ("Your action (arg2) is incorrect", file=sys.stderr)
                issue = True
        if not ((sort_direction == 'forward') or (sort_direction == 'reverse')):
                print ("Your direction arg(3) is incorrect", file=sys.stderr)
                issue = True
else:
        issue=True
        print("Too many arguments: must have 3 or 4 command line arguments", file=sys.stderr)

if issue:
	print("Incorrect Usage: python3 books1.py input-file action [sort-direction]\ninput-file = the file you would like to read\naction = \"books\" or authors\"\n[sort-direction] = reverse or forward (defaults to forward).", file=sys.stderr)

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

        author_list.sort(key = get_last_name) #sorts the list by last name
        if sort_direction == "reverse": #if it needs to be reversed
            author_list.reverse() #reverse it
        for author in author_list: #print the authors
            print(author)

    else: #fail statement (Should now never occur)
        print("you didn't write 'books' or 'authors'!")

