grade = 100
str_input = input("Enter your score : ")
grade = int(str_input)

if grade == 100:
    print("Perfect")

elif grade >= 75:
    print("Not bad")

elif grade >= 50:
    print("Poor :(")

    if grade <= 50:
        print("But, you need improve it!")
    else:
        print("With greater score")

else:
    print("Score not found !")
