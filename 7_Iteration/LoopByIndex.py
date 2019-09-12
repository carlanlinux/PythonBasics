'''By using the enumerate function, we can print out a counter that tells us
 the position of an item in a list. We could do this ourselves, but this saves
  us from having to do that. The index positions in the list are 0, 1 , 2, 3, and 4
  . This is exactly the same sequence of integers that are stored in counter each
  time the loop is iterated. The first time through the for loop, counter will be 0
   and “apple” will be printed. Then, counter will be reassigned to 1 and “pear” will
   be displayed. This will continue until the list has ended, so that the final value
   for counter will be 4 and the final value of item will be “peach”.'''

for counter, item in enumerate(['apple', 'pear', 'apricot', 'cherry', 'peach']):
    print(counter, item)