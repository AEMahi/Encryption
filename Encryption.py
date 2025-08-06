# Annotate all functions and inputs with data types
# PEP8 Standard for Python

from random import choice

# Change this to all lowercase
Splitter = u'\u2964'

def get_task():
    task = input('Encrypt, Decrypt, or Quit? ')
    task = task.lower()
    while task != 'encrypt' and task != 'decrypt' and task != 'quit':
        task = input('You need to put Encrypt, Decrypt, or Quit: ')
        task = task.lower()
        if task == 'encrypt' or task == 'decrypt'or task == 'quit':
            return task
    if task == 'encrypt' or task == 'decrypt'or task == 'quit':
        return task
    
def get_message():
    message = input('Enter the message: ')
    return message

def is_even(number):
    return number % 2 == 0

def get_even_letters(message: str):
    # This can be replaced with a list comprehension: https://youtu.be/3dt4OGnU5sM?si=OcUfCMShyIC1l2AG
    even_letters = []

    # This pattern is "non-pythonic" - you can loop directly through the list
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even (counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + Splitter
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def mapping(message):
    letter_list = []
    # Replace below with a python package rather than literal
    from_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    to_list = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
    word = list(message)
    for counter in range(0, len(word)):
        if word[counter] in from_list:
            to_index = from_list.index(word[counter])
            to_letter = to_list[to_index]
            letter_list.append(to_letter)
        else:
            letter_list.append(word[counter])
    New_message = ''.join(letter_list)
    return New_message

def encrypt(message):
    encrypted_list = []
    fake_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    swapped_letters = swap_letters(message)
    for counter in range(0,len(swapped_letters)):
        encrypted_list.append(swapped_letters[counter])
        encrypted_list.append(choice(fake_letters))
    fake_letter_message = ''.join(encrypted_list)
    new_message = mapping(fake_letter_message)
    encrypted_message = ''.join(reversed(new_message))
    return encrypted_message

def decrypt(message):
    unreversed_message = ''.join(reversed(message))
    mapped_message = mapping(unreversed_message)
    even_letters = get_even_letters(mapped_message)
    unswapped_letters = swap_letters(even_letters)
    new_message = ''.join(unswapped_letters)

    if Splitter in new_message:
        parts = new_message.split(Splitter)
        if '' == parts[1]:
            new_message = parts[0]
    return new_message

def main() -> None:
    while True:
        task = get_task()
        if task == 'encrypt':
            message = get_message()
            encrypted = encrypt(message)
            print('Ciphertext is: ', encrypted)
        elif task == 'decrypt':
            message = get_message()
            decrypted = decrypt(message)
            print('Decrypted text is: ', decrypted)
        elif task == 'quit':
            break

if __name__ == '__main__':
    main()