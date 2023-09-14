import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = ""
while direction != "encode" and direction != "decode":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text = ""
while not text.isalpha():
    text = input("Type your message:\n").lower()

shift = 0
while shift < 0 or shift == 0:
    shift = int(input("Type the shift number:\n"))

def ceaser(text, shift, direction):
    final_text = ""
    for letter in text:
        # get index of letter in alphabet, add to shift for cipher index
        idx = alphabet.index(letter)
        if letter.isalpha():
            if direction == "encode":
                if (idx + shift) > 25:
                    new_idx = (idx + shift) - (len(alphabet))
                    final_text += alphabet[new_idx]
                else:
                    final_text += alphabet[idx + shift]
            else:
                final_text += alphabet[idx - shift]
        else:
            final_text += letter


    print(f"The {direction}d text is {final_text}")

# end_cipher = ""
# while end_cipher != "yes" and end_cipher != "no":
#     end_cipher = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
# if end_cipher == "yes":
#     ceaser(text, shift, direction)
# else:
#     print("Goodbye")

ceaser(text, shift, direction)