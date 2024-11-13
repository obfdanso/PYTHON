# import random
# Simple function
    # def greet():
    #     print("Good morning")
    #     print("Good afternoon")
    #     print("Good evening")

    # greet()

# Functions with input
    # name = ["Samuel","Solomon","Eric","Prince","Daniel","Comfort","Paul","Dinah"]
    # n_name = random.choice(name)
    # def greet_with_name(n_name):
    #     print(f"Good morning {n_name}")
    #     print(f"Good afternoon {n_name}")
    #     print(f"Good evening {n_name}")
    # greet_with_name(n_name)

# Functions with more than one input
    # location = ["Accra","Chicago","London","Kumasi","Ohio"]
    # n_location = random.choice(location)
    # def greet_with(n_name, n_location):
    #     print(f"Hello {n_name}")
    #     print(f"What is it like in {n_location}?")
    # greet_with(n_name, n_location)

# Functions with keyword arguments
    # def greet_with_keyword(name, location):
    #     print(f"Hello {name}")
    #     print(f"What is it like in {location}")
    # greet_with_keyword(name = "Danso",location = "USA" )

# Area calculation
    # test_h = int(input("Height of wall: "))
    # test_w = int(input("Width of wall: "))
    # coverage = 5
    # import math

    # def paint_calc(height, width, cover):
    #      ans = math.ceil((test_h * test_w / coverage))
        
    #      print(f"You would need {ans} cans")
        
    # paint_calc(height = test_h, width = test_w, cover = coverage)
# Prime number checker
    # def prime_checker(number):
    #     prime = True
    #     for i in range(2, number):
    #        if number % i == 0:
    #            prime = False
    #     if prime == True:
    #         print("It is prime")
    #     else:
    #         print("It is not prime")
    
# n = int(input("Check this number: "))   
# prime_checker(number = n)

# Caesar Cipher
    # alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] * 2
    # should_continue = True
    # while should_continue:
    #     direction = input("Type 'encode' to encrypt or 'decode'to decrypt:\n")
    #     text = input("Tpye your message:\n").lower()
    #     shift = int(input("Type your shift number:\n"))
    #     shift = shift % 26
#  First trail
    # def encrypt(text, shift):
    #     cipher_text = ""
    #     for letter in text:
    #         pos = alphabet.index(letter)
    #         new_pos = shift + pos
    #         new_letter = alphabet[new_pos]
    #         cipher_text += new_letter
    #     print(f"The encoded text is {cipher_text}")


    # def decrypt(text, shift):
    #     decipher_text = ""
    #     for letter in text:
    #         pos = alphabet.index(letter)
    #         new_pos = pos - shift
    #         new_letter = alphabet[new_pos]
    #         decipher_text += new_letter
    #     print(f"The decoded message is {decipher_text}")

    # if direction == "encode":
    #     encrypt(text,shift)
    # elif direction == "decode":
    #     decrypt(text,shift)
    # else:
    #     print("You input is invalid")
    
 # def caeser(text, shift, direction):
    #     end_text = ""
    #     for letter in text:
    #         pos = alphabet.index(letter)
    #         if  direction == "encode":
    #             new_pos = shift + pos
    #             new_letter = alphabet[new_pos]
    #             end_text += new_letter

    #         elif direction == "decode":
    #             new_pos = pos - shift
    #             new_letter = alphabet[new_pos]
    #             end_text += new_letter
    #         else:
    #             print("Direction given is invalid")
        

    #     if direction == "encode":
    #         print(f"The encoded message is {end_text}")
    #     elif direction == "decode":
    #         print(f"The decoded message is {end_text}")
    #     else:
    #         print("Direction given is invalid")
   
    # caeser(text, shift, direction)
    # result = input("Type 'yes' to continue and 'no' to stop\n")
    # if result == "no":
    #     should_continue = False
    #     print("Goodbye")