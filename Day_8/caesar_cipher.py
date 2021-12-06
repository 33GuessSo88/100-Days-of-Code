alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift = shift % 26
    result = input("Do you want to continue, yes or no?")
    if result == "no":
        should_ontinue = False
        print("Goodbye")

def caesar(input_text, shift_amount, input_direction):
    output_text = ""
    for letter in input_text:
        if letter in alphabet:
            input_text_position = alphabet.index(letter)
            if input_direction == "encode":
                cipher_text_position = input_text_position + shift_amount
                if cipher_text_position <=25:
                    output_text += alphabet[cipher_text_position]
                else:
                    cipher_text_position = cipher_text_position - 26
            if input_direction == "decode":
                input_text_position = alphabet.index(letter)
                plain_text_position = input_text_position - shift_amount
                if plain_text_position < 0:
                    plain_text_position = plain_text_position + 26
                    output_text += alphabet[plain_text_position]
                else:
                    output_text += alphabet[plain_text_position]
        else:
            output_text += letter
    
    print(f"Your {input_direction}d text is {output_text}")

caesar(input_text=text, shift_amount=shift, input_direction=direction)

# def encrypt(plain_text, shift_amount):
#     cipher_text = []
#     for letter in plain_text:
#         plain_text_position = alphabet.index(letter)
#         #print(plain_text_position)
#         cipher_text_position = plain_text_position + shift_amount
#         if cipher_text_position <= 25:
#             #print(cipher_text_position)
#             cipher_text.append(alphabet[cipher_text_position])
#         else:
#             cipher_text_position = cipher_text_position - 26
#             cipher_text.append(alphabet[cipher_text_position])
#         #print(cipher_text)
#     cipher_string = ''.join(map(str, cipher_text))
#     print(cipher_string)

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         cipher_text_position = alphabet.index(letter)
#         plain_text_position = cipher_text_position - shift_amount
#         if plain_text_position < 0:
#             plain_text_position = plain_text_position + 26
#             plain_text += alphabet[plain_text_position]
#         else:
#             plain_text += alphabet[plain_text_position]
#     print(plain_text)

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("you typed something wrong")
