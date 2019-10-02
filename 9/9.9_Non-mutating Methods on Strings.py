'''
upper is a method that can be invoked on any string object to create a new string in which all the characters are in uppercase.
lower works in a similar fashion
http://docs.python.org/3/library/stdtypes.html#string-methods
'''

ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)

ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***"+ss.strip()+"***")

news = ss.replace("o", "***")
print(news)

#No usar + para concatenar cadenas, mejor utilizar comodines {} y luego darle formato al final
#MAL
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))

#BIEN:
#fill-in-the-braces. The string method format, makes substitutions into places in a string enclosed in braces.

scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))


person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)

#For two decimal places, put :.2f inside the braces for the monetary values:
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)

#
name = "Sally"
greeting = "Nice to meet you"
s = "Hello, {}. {}."

print(s.format(name,greeting)) # will print Hello, Sally. Nice to meet you.

print(s.format(greeting,name)) # will print Hello, Nice to meet you. Sally.

print(s.format(name)) # 2 {}s, only one interpolation item! Not ideal.

#Si se quiere imprimir {} para que no lo interprete mal hay que poner dobles {{
a = 5
b = 9
setStr = 'The set is {{{}, {}}}.'.format(a, b)
print(setStr)