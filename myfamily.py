myfamily = ("mother", "father", "sister", "brother", "sister") 

print(myfamily)
print(type(myfamily))
print(myfamily[2])

# Will not work, since tuples are not mutable
myfamily.append("me")
myfamily.pop(3)