# File: password.py
# Author: Mia Marche
# Date: 2/12/2022
# Section: 589
# E-mail: miamarche@tamu.edu
# Description: This program generates a password for the user.
print("Welcome to the Library Management App.")
print("Password generation")
last_name = input("Enter the member's last name: ")
phone = input("Enter the member's phone number: ")
address = input("Enter the member's mailing address: ")
first_digit = phone[:1]
vowel_a = int(last_name.lower().count("a"))
vowel_e = int(last_name.lower().count("e"))
vowel_i = int(last_name.lower().count("i"))
vowel_o = int(last_name.lower().count("o"))
vowel_u = int(last_name.lower().count("u"))
vowel_count = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
vowel_count = str(vowel_count)
name_length = len(last_name)
# By finding the length (len()) of the word and subtracting 1 from that
# you can get the last character of the input
last_letter = last_name[name_length-1:].upper()
phone_replaced = phone.replace(f"{first_digit}", f"{last_letter}")
first_part_password = vowel_count + phone_replaced
zip_code = address.split(sep=", ")
zip_code = zip_code[2]

zip_code_reversed = zip_code[-4:]
zip_code_reversed = zip_code_reversed[::-1]

second_part_password = first_part_password + zip_code_reversed
house_number = address.split()[0]
digit1 = int(house_number[:1])
digit2 = int(house_number[1:2])
digit3 = int(house_number[2:])
digit1 = digit1 % 2
digit2 = digit2 % 2
digit3 = digit3 % 2
password = second_part_password + str(digit1) + str(digit2) + str(digit3)
print("")
print(f"Generated password: {password}")
