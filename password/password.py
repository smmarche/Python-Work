#This program reads a file passwords.txt that contains multiple passwords 
#and checks the validity of the passwords.

def validate(password):
    """Validates a password a returns a boolean that determines if the password is valid of invalid"""
    is_valid = False
    # To be completed ...
    length = len(password)
    if 4 <= length <= 8:
        is_valid = True
        if any(char.isdigit() for char in password):
            is_valid=True
        else:
            is_valid= False
    return is_valid




def main():
    """ Reads the password files and check for the validity of every password."""
    with open('passwords.txt', 'r') as data:
        line = data.read()
        list_of_words = line.split()
    for word in list_of_words:
        if validate(word):
            print(f"{word} is valid")
        else:
            print(f"{word} is invalid")



main()
