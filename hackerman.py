a, b = 1, 2
#print(a, b)

# 1 gets assigned to a and 2 gets assigned to b

#    1, 2 # 1.a

#print((a, b))
#same as 1 # 1.b
a, b = b, a
#print(a, b)

# 1 and 2 change positions # 1.c
a, b = b, a
#print(a, b)
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