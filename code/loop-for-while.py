n = int(input("Input max data : "))
i = 0

for i in range(n):
    j = 0

    while j < n - i:
       print("*", end=" ")
    j += 1

print()

# This code can causing lag...


