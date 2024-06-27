import random
import string

def password_generator(n, characters):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    everything = letters + digits + symbols

    if characters == "letters":
        char_set = letters
    elif characters == "digits":
        char_set = digits
    elif characters == "symbols":
        char_set = symbols
    elif characters == "all":
        char_set = everything
    else:
        raise ValueError("Invalid character type specified. Use 'letters', 'digits', 'symbols', or 'all'.")

    password = ''.join(random.choice(char_set) for _ in range(n))
    return password


no_of_values = int(input('Enter the number of characters required to create a password: '))
if no_of_values <= 0:
    raise ValueError("The number of characters must be positive.")

character_type = input("Enter the type of characters to use (letters, digits, symbols, all): ").lower()
print(password_generator(no_of_values, character_type))
