grade = 100
str_input = input("Input your score :")
grade = int(str_input)

if grade == 100:
    print("Perfect")
elif grade >= 75:
    print("Not bad")
elif grade >= 50:
    print("Poor :(")
else:
    print("Error : Score not found !")

