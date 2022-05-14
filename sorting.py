# This program sorts books alphabetically, year published, and barcode number.


#ask the user for how many books they will enter
number_book_titles = int(input("Enter the number of book titles: "))
print()
book_title_number = 1
#empty lists below will store information the user inputs about the book within the loop
book_counter = number_book_titles
book_information = []
alpha_book_sort =[]
year_published_sort = []
barcode_sort = []
while book_counter > 0:
    book_name = input(f"Book title #{book_title_number}: ")
    year_published = int(input(f"Book ({book_name}) publication year: "))
    barcode = input(f"Book ({book_name}) barcode string: ")
    book_title_number += 1
    book_counter -= 1
    print()
    book_information.append([book_name, year_published, barcode])
    alpha_book_sort = sorted(book_information)
    #Reverse sort by the second element in the list(publication)
    year_published_sort = sorted(book_information, key=lambda x: x[1], reverse=True)
    barcode_sort = sorted(book_information, key=lambda record: max(int(n) for n in record[2].split()))

print("Sorted books by title:")
print()
#Uses a for loop to sort through the list of lists by title alphabetically and prints them out
for book in alpha_book_sort:
    print(f"{book[0]}\nPublished in: {book[1]}\nBarcode string: {book[2]}")
    print()
#Uses a for loop to sort through the list of lists by year and prints them out
print("Sorted books by publication year:")
print()
for book in year_published_sort:
    print(f"{book[0]}\nPublished in: {book[1]}\nBarcode string: {book[2]}")
    print()
#Use def above to sort by max number in barcode
print("Sorted books by barcode string maximum number:")
print()

for book in barcode_sort:
    print(f"{book[0]}\nPublished in: {book[1]}\nBarcode string: {book[2]}")
    print()


