def sort(a, b):
    if b < a:
        a, b = b, a
    return a, b


def run():
  a = input("Enter Your First Number ")
  b = input("Enter Your Second Nnumber ")
  print(', '.join(sort(a, b)))
