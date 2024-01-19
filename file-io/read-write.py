with open("text.txt", "r+", encoding="utf-8") as f:
   print(f"read:\n{f.read()}")
   f.write("lorem ipsum dolor\n")
   print(f"read:\n{f.read()}")

with open("text.txt", "r+", encoding="utf-8") as f:
   print(f"read:\n{f.read()}")
