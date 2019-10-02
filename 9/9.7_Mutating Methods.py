'''
9.7. Mutating Methods
Mutating methods are ones that change the object after the method has been used. Non-mutating methods do not change the
 object after the method has been used.

 count and index methods are both non-mutating. Count returns the number of occurances of the argument given but does
 not change the original string or list.

index returns the leftmost occurance of the argument but does not change the original string or list.
http://docs.python.org/py3k/library/stdtypes.html#sequence-types-str-bytes-bytearray-list-tuple-range
'''

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)