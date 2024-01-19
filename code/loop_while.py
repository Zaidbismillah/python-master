should_continue = True

while should_continue:
    n = int(input("Input an even number greater than 0 : "))

    if n <= 0 or n % 2 == 1:
        print(n, "Is not an even number greater than 0 ")
        should_continue = False
    else:
        print("number : ", n)
