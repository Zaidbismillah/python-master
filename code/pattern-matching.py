# match + case = pattern matching
# match & case = if

command = input("Enter command : ")
match command:

   case "greet":
    name = input("Your name : ")
    print("Hello", name)

   case "sum_numbers":
    numbers = input("The numbers separated by space : ")
    total = 0
    for str in numbers.split(' '):
     total = total + int(str)
    print("total:", total)

   case "lucky_number":
    import random
    n = random.randint(0, 100)
    print("your lucky number :", n)

   case _:
    print("unrecognized command")
