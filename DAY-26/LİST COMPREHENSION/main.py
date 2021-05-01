
# Challenge 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if num % 2 == 0]

print(result)



# Challenge 2
import pandas

with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(i.strip()) for i in file1_data if i in file2_data]
print(result)
      

  




