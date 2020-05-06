import re
s=input("enter pattern to check:")
m=re.fullmatch(s,"ababab")
if m!=None:
   print("Full string matched")
else:
   print("Doesnot mathced full string") 