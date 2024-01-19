def inspec_data(data):
   if data == None:
    print("data is empty. like very empty")
   else:
     print(f"data: {data}, type: {type(data).__name__}")

data = 0
inspec_data(data)
# output > data: 0, type: int

data = ""
inspec_data(data)
# output > data: , type: str
