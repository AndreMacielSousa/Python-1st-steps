#Loop Idoms
from itertools import count


print("Maior da Lista")
largest = -1
print("Before:", largest)
for x in [9, 41, 12, 3, 74, 15]:
    if x > largest: 
        largest = x
    print(largest, x)
print("after", largest)

# Exercicio Qual o erro ?
print("\nMais Pequeno")
smallest = None
print("Before:", smallest)
for itervar in [9, 41, 12, 3, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
#        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

#contagem
print("\nContagem")
zork = 0
print("Before:", zork)
for x in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
print("After:", zork)

#soma
print("\nSOMA")
zork = 0
print("Before:", zork)
for x in [9, 41, 12, 3, 74, 15]:
    zork = zork + x
print("After:", zork)

#media
print("\nMedia")
cont = 0
sum = 0
print("Before:", cont, sum)
for x in [9, 41, 12, 3, 74, 15]:
    cont = cont + 1
    sum = sum + x
print("After:", cont, sum, sum/cont)

# Boolean Seach
print("\nBoolean Search")
found = False
print("Before", found)
for x in [9, 41, 12, 3, 74, 15]:
    if x == 3: found = True
    print(found, x)
print("After", found)

