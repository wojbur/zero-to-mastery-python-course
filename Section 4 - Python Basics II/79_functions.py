def say_hello():
    print('helooo')

def show_tree(fill, empty=" "):
    for row in PIC:
      for pixel in row:
        if pixel:
          print(fill, end="")
        else:
          print(empty, end="")
      print("")


PIC = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


# show_tree("*")
# show_tree("o")
# show_tree("@")
show_tree("")
