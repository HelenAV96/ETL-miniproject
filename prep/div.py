a, b = 1, 2
print(a, b)

# 1 gets assigned to a and 2 gets assigned to b

#    1, 2 # 1.a

print((a, b))
#same as 1 # 1.b
a, b = b, a
print(a, b)

# 1 and 2 change positions # 1.c
a, b = b, a
print(a, b)
# 1 and 2 change position again # 1.d

a, b, c = 1, 2, 3
#print(a, b, c)
#1 gets assigned to a, 2 to b, 3 to c# 1.e
a, b, c = b, c, a
print(a, b, c)
#  ORder of assigned values is reversed # 1.f
a, b, c = b, c, a
print(a, b, c)
# Order of assigned values are changed once again.   ??? # 1.g




#2. do and explain the following:
def dup():
  return 1, 2
#2a
#the function returns 1 and 2. a,b are calling on the same function
a, b = dup()
print(a, b)

#2b
#this assigns the function to a so a becomes '(1,2)' and b is still 2
a = dup()
print(a, b)


   
#3. # iterator over a dictionary:

d = { 'a': 1, 'b': 2, 'y': 3 }
for key, value in d.items():
    print(key, value)
#    prints key and value in dictionary, a 1, b 2, y 3 # 3.a

for keyval in d.items():
    print(keyval)
#   prints key-value pair, ('a', 1) etc. # 3.b

for keyval in d.items():
    print(keyval[0], keyval[1])

#    iterates through key-value pairs in dictionary and prints each pair # 3.c

for keyval in d.items():
    key, val =  keyval
    print(key, val)
    
#    iterates, prints key and value # 3.d