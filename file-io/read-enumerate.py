with open("text.txt", "r", encoding="utf-8") as f:
  for i, line in enumerate(f):
   print(f"line {i+1}: {line}")
