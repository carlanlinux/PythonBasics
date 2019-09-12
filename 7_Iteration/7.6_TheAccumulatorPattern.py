'''The anatomy of the accumulation pattern includes:

        initializing an “accumulator” variable to an initial value (such as 0 if accumulating a sum)
        iterating (e.g., traversing the items in a sequence)
        updating the accumulator variable on each iteration (i.e., when processing each item in the sequence)

#Si queremos usar la función Range tiene que ser dentro de un list() casteado. Range sólo sirve en un for. '''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)

