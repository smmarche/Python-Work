
# The program outputs the member’s formatted information.

print("Welcome to the Library Management App.")
print("Member registration")
first_name = input("Enter the member's first name: ")
middle_name = input("Enter the member's middle name: ")
last_name = input("Enter the member's last name: ")
phone = str(input("Enter the member's phone number: "))
address = input("Enter the member's mailing address: ")
first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()
print("")
phone1 = str(phone[:3])
phone2 = str(phone[4:7])
phone3 = (phone[8:])
phone = phone1 + phone2 + phone3
international_phone = "+1-" + phone1 + "-" + phone2 + "-" + phone3
american_phone = "(" + phone1 + ") " + phone2 + "-" + phone3
local_phone = phone2 + "." + phone3
house_number = address[:3]
street_name = address.split(",")[0]
street_name = street_name[4:].upper()
city = address.split(",")[1].upper()
state = address.split(",")[2]
state = state[:3].upper()
zipcode = address.split(",")[2]
zipcode = zipcode[4:]
# or try \n here
print("Member name:", first_name, middle_name, last_name)
print(f"Phone number (International format): {international_phone}")
print(f"Phone number (North American format): {american_phone}")
print(f"Phone number (Local format): {local_phone}")
print(f"Street number: {house_number}")
print(f"Street name: {street_name}")
print(f"City:{city}")
print(f"State:{state}")
print(f"Zip: {zipcode}")
