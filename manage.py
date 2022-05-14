# File: manage.py
# Author: Mia Marche
# Date: 3/22/2022
# Section: 589
# E-mail: miamarche@tamu.edu
# Description: This program gets the book information from the user store and prints them.
book_information = {}
#!?WHAT IF USER ENTERS DONE AT ANY LEVEL?
input_not_done = True
#The while loop below allows the menu options to keep repeating
while input_not_done:
#Book type is collected
    book_type = input("Enter book type: ").title()
#Checks to see if Done is typed (if done is typed the loop is stopped)
    if book_type == "Done":
        input_not_done = False
#If something other than done is typed then more information will be collected.
    else:
        book_title = input("Enter book's title: ").title()
        publication_year = int(input("Enter book's publication year: "))
        author = input("Enter book's first author's name: ").title()
        publisher = input("Enter book's publisher name: ").title()
        print()
#Grouping the genre by different dictionaries i.e. {fiction: {}}
        if book_type not in book_information:
            book_information[book_type] = {}
#Setting the publication year as the value and a key
        if publication_year not in book_information[book_type]:
            book_information[book_type][publication_year] = [[book_title, author, publisher]]
        # {romance: {1997:[[Maths, Jack, A&M]]}}
        else:
            book_information[book_type][publication_year].append([book_title, author, publisher])


print()
#Retrieve and print the genre, year, title, author, and publisher by using .items, .keys,
# and indexing
for key, information in book_information.items():

    print(f"===={key}")
    for year in book_information[key].keys():
        print(f"Published in {year}:")
        print(f"{'Title':<15}|{'Author':<15}|{'Publisher':<15}|")
        for item in book_information[key][year]:
            print(f"{item[0]:<15}|{item[1]:<15}|{item[2]:<15}|")
        print()





