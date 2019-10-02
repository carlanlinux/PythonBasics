#Con append añades en la nueva lista, con concat creas una lista nueva duplicando la anterior y añadiendo lo que sea.

#IMPORTANTE: In order to use concatenation, we need to write an assignment statement that uses the accumulator pattern:

origlist = [45,32,88]
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list before changes
newlist = origlist + ['cat']
print("newlist:", newlist)
print("the identifier:", id(newlist))              #id of the list after concatentation
origlist.append('cat')
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list after append is used

#OJO:  Error, you cannot concatenate a list with an integer.
# += en listas es como append
origlist1 = [45,32,88]
aliaslist = origlist
origlist1 += ["cat"]
origlist1 = origlist1 + ["cow"]