# Built-in imports
import math

# Your code below
GRADE = {}
for x in range(101):
  if x >= 70:
    GRADE[x] = "A"
  elif x >= 60:
    GRADE[x] = "B"
  elif x >= 55:
    GRADE[x] = "C"
  elif x >= 50:
    GRADE[x] = "D"
  elif x >= 45:
    GRADE[x] = "E"
  elif x >= 40:
    GRADE[x] = "S"
  else:
    GRADE[x] = "U"

def read_testscores(filename):
  """
  """
  lst = []
  with open(filename ,'r') as f:
    for x in f:
      store = {}
      data = f.readline().strip().split(",")
      store["class"] = data[0]
      store["name"] = data[1]
      overall = math.ceil(int(data[2]) /30 * 15 + int(data[3]) /40 * 30 + int(data[4]) /80 * 35 + int(data[5]) /30 * 20)
      store["overall"] = overall
      store["grade"] = GRADE[overall]
      lst.append(store)
    return lst


def analyze_grades(studentdata):
  """
  """
  store = {}
  for x in studentdata:
    x = list(x.values())
    if x[0] not in store.keys():
      store[x[0]] = {x[3] : 1}
    elif x[3] in store[x[0]].keys():
      store[x[0]][x[3]] += 1
    else:
      store[x[0]][x[3]] = 1
  return store
      
   
  
    