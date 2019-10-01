#IS operator - We can test whether two names refer to the same object using the is operator.
#Python assigns every object a unique id and when we ask a is b what python is really doing is
# checking to see if the id(a) == id(b).

a = "banana"
b = "banana"

print(id(a))
print(id(b))

a = "banana"
b = "banana"

print(a is b)

#ESto pasa porque son String, en el caso de listas por ejemplo no ocurriría así, cada lista es un objeto distinto
a = [81,82,83]
b = [81,82,83]

print(a is b)

print(a == b)

print(id(a))
print(id(b))