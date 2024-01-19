note = "the module to calculate contains mathematic functions"
def calc_hypotenuse(a, b):
  return sqrt(pow(a) + pow(b))

def pow(n, p = 2):
  return n ** p

def sqrt(x):
  n = 1
  for _ in range(10):
   n = (n + x/n) * 0.5
  return n

# Use this command to call the modules (in terminal)
# "python calculate.py"

# Use this code to call the modules (in same directory with the code)
# import calculate
