a = input("Password:")

if (len(a)>10) or (len(a) <= 20):
  print("CORRECT")
else:
  print("Password must be between 10 and 20 characters")
