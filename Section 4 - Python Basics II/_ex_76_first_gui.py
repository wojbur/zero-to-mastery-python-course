picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for row in picture:
  string = ""
  for char in row:
    if char == 0:
      string += " "
    else:
      string += "*"
  print(string)

# iterate over picture
#   if 0 -> print ""
#   if 1 -> print "*"

for row in picture[::-1]:
  for item in row:
    if item == 0:
      print(" ", end="")
    else:
      print("*", end="")
  print("")
