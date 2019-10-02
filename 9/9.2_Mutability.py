alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y'] #OJo! si usamos los dos puntos se pueden coger varios
print(alist)

#Resultado ['a', 'x', 'y', 'd', 'e', 'f']: Importante cambia la posición:
#Numero1:Numero2 --> Num1: posición en la que empieza a sustituir/borrar Num2: últimoNumero que borra/sustitiye


phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + "the night sky." #Añades letra al principio
excited_phrase_complete = phrase_complete[:-1] + "!" #Añades letra al final

# the key difference between lists and tuples: tuples are like immutable lists. Once a tuple is created, it can’t be changed.

a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)