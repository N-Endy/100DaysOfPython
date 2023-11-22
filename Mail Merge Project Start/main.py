with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
        
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as send_letter:
            send_letter.write(new_letter)