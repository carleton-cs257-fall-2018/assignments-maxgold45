import csv

input_file = input("Input file? ")
sort_direction = input("Sort direction? 'reverse', 'forward', or empty (defaults to forward) ")
action = input("Action? 'books' or 'authors' ")

#these inputs would normally come from the command line, using normal python input for now
#also needs error checking and failure statement as described in instructions

#sets the dialect to unix, dialect is just rules for separating entries 
unix_dialect = csv.get_dialect("unix")
#with statement means we don't have to use .close? I think.
#NOTE: The argument 'encoding="UTF-8"' means 
with open(input_file, newline='', encoding="UTF-8") as csvfile:
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

        #!!! note: current issues: 
        #does not sort by last name (use sort key = with a custom function getLastNameFirstLetter)
        #does not allow special characters (use a better data structure than strings? or maybe the print function is confused?)
        #does not get rid of 'and' before Terry Pratchett's name (need to do that manually)
        
        author_list.sort() #sorts the list
        if sort_direction == "reverse": #if it needs to be reversed
            author_list.reverse() #reverse it
        for author in author_list: #print the authors
            print(author)

    else: #fail statement (should be better)
        print("you didn't write 'books' or 'authors'!")
