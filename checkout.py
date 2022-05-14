
# This module prints a menu repeatedly for a user to check out
# books from the library until the user quits the program.
#Program repeats until the user enters quit so used a while loop
quit_menu = False
capitalize_book_collection = {}
while not quit_menu:
#Menu prompts
    print("1. Add a book to the cart")
    print("2. Remove book(s) from the cart")
    print("3. View cart")
    print("4. Sort cart")
    print("5. Quit")
    print("")
#Receiving menu prompt, if user enter number other than what was listed, the loop
#repeats
    menu_selection = int(input("Select from menu: "))
#Set up different categories for various input options
    if menu_selection == 1:
        #Use .lower() on book_title to catch duplicates within
        # the key due to lack of case sensitivity
        book_title = input("Book title: ").lower()
        book_title_capitalize = book_title.title()
#Checked to see if there were duplicates already in the cart
        if book_title_capitalize in capitalize_book_collection:
            print("This book is in your cart.")
        else:
            capitalize_book_title = book_title.title()
            author = input("Book author's name: ")
            capitalize_author = author.title()
            day = int(input("How many days: "))
#Added information to a dictionary
            capitalize_book_collection[capitalize_book_title] = [capitalize_author, day]

        print()
    elif menu_selection == 2:
        remove_book = input("Remove all or an item? (Enter 'all' or 'book title'): ").title()
    #Remove everything from the dictionary
        if remove_book == "All":
            capitalize_book_collection.clear()
    #Removed the book the user requested from the dictionary
        elif remove_book in capitalize_book_collection.keys():
            del capitalize_book_collection[remove_book]
    #Otherwise, the book isn't even in the dictionary so just told the user this
        else:
            print(f"{remove_book} is not in your cart.")
        print()
    #Print what is in the dictionary
    elif menu_selection == 3:
    #Separated by a non-empty cart and an empty cart
    #If the cart has something in it the header and items are printed
        if capitalize_book_collection:
            print(f"{'Title':<20}{'Author':<20}{'Period':<20}")
            for book, values in capitalize_book_collection.items():
                print(f"{book:<20}{values[0]:<20}{values[1]:<20}")
            print()
    #Otherwise, tell the user the cart is empty
        else:
            print("The cart is empty.")
            print()
    #Organize the info received prior to making this selection
    elif menu_selection == 4:
        if capitalize_book_collection:
            sort_choice = input("Enter 'A' for Ascending and 'D' for Descending: ").title()
            if sort_choice == "A":
                alpha_book_collection = {}
    #Sort the books by the title in alphabetical order
                for title in sorted(capitalize_book_collection, reverse=False):
                    alpha_book_collection[title] = capitalize_book_collection[title]
                print(f"{'Title':<20}{'Author':<20}{'Period':<20}")
                for book, values in alpha_book_collection.items():
                    print(f"{book:<20}{values[0]:<20}{values[1]:<20}")
                print()
            elif sort_choice == "D":
    #Sort the books by title in reverse alphabetical order
                reversed_alpha_book_collection = {}
                for title in sorted(capitalize_book_collection, reverse=True):
                    reversed_alpha_book_collection[title] = capitalize_book_collection[title]
                print(f"{'Title':<20}{'Author':<20}{'Period':<20}")
                for book, values in reversed_alpha_book_collection.items():
                    print(f"{book:<20}{values[0]:<20}{values[1]:<20}")
                print()
#The cart is empty otherwise
        else:
            print("This cart is empty.")
            print()
#Exit the loop upon request
    elif menu_selection == 5:
        quit_menu = True

