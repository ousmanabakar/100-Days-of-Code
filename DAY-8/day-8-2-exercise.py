#Write your code below this line 👇
def prime_checker(n):

  for i in range(2,n):
    
    if n % i== 0:
      print("It's not a prime number.")
      break
  else:
    print("It's a prime number.")







#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(n)



