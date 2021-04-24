name_list = []

with open("./Input/letters/starting_letter.txt") as letter:
    with open("./Input/Names/invited_names.txt", "r") as names:
        for name in names:
            new_name = name.strip()
            name_list.append(new_name)

    example_message = letter.read()
    for i in name_list:
        new_message = example_message.replace("[name]", i)
        with open(f"./Output/ReadyToSend/letter_for_{i}.txt", "w") as ReadyToSend:
            ReadyToSend.write(new_message)
