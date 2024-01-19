def get_hello_message1():
  return "hello python"

res = get_hello_message1()
print(res)
# output > hello python

get_hello_message2 = lambda : "hello python"
res = get_hello_message2()
print(res)
# output > hello python
