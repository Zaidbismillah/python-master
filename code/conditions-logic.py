grade = int(input("Input your score : "))
prev_grade = int(input("Input your previous score : "))

if grade >= 100 and prev_grade >= 75:
    print("Awesome")

if grade >= 100 and prev_grade < 50:
  print("Awesome. you definitely working hard, right?")
elif grade >= 50:
 print("passed the exam")

else:
     print("below the passing grade")

if (grade >= 50 and not prev_grade >= 50) or (not grade >= 50 and
prev_grade >= 50):
   print("at least you passed one exam. good job!")
