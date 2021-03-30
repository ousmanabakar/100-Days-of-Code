from art import logo
print(logo)

#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply  
def multiply(n1, n2):
  return n1 * n2

#division
def division(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : division
}

def calculator():  
  num1 = float(input("What is the first number?: "))

  for key in operations:
    print(key)

  while True:
  
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))

    calculation_func = operations[operation_symbol]
    first_answer = calculation_func(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    response = input(f"Type 'y' to continue calculating with {first_answer}, type 'n' to start a new calculation.: ")
    if response =="y":
      num1=first_answer

    else:
      calculator()

calculator()
