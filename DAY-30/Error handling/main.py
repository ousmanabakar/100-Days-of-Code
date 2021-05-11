# TypeError
# text = "abc"
# print(text + 5)

# IndexError
# names = ["Ali", "Yusuf", "Veli"]
# name = names[3]

# keyError
# a_dict ={"one": 1}
# value = a_dict["two"]


# FileNotFoundError
# try:
#     file = open("abc.txt")
#     a_dict = {"one": 1}
#     #print(a_dict["two"])
#     print(a_dict["one"])
# except FileNotFoundError:
#     file = open("abc.txt", "w")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()
#     print("file was closed")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = weight / (height * height)
print(bmi)

