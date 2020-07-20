"""
Problems involving scope
"""

# FIXME: Section 1: Fix this function so that it prints the local variable.

def iceCream():
  x = "My favorite flavor is cookie dough."
  print()

iceCream(x)


# FIXME: Section 2: Fix this function so that it prints the global variable instead of the local variable. 

y = "Pineapple is my favorite fruit." 

def fruit():
  y = "Mango is my favorite fruit."
  print(y)

fruit()


# FIXME: Section 3: Fix the function so that it prints both variables.

n = "Stranger Things"
def Netflix():
  global n
  print(n)
  n = "Avatar the Last Airbender"
Netflix()
