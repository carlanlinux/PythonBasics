
'''
Asignar una variable el valor de otra el objeto es el mismo.
Because the same list has two different names, a and b, we say that it
is aliased. Changes made with one alias affect the other.
Python is free to alias strings and integers when it sees an opportunity to economize.
'''

a = [81, 82, 83]
b = a
print(a is b)

a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)
