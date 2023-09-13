#Comprimento
#fruit = input("Escolha uma Fruta: ")
fruit="CTMBJT86L1B602826312-LE-032022-12-050008601086"
print("Comprimento ", fruit," ", len(fruit))
'''
print("Looping While to ", fruit)
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1

print("Looping FOR to ", fruit)
for letter in fruit: print(letter)


def conta(letter, word):
    count = 0
    for x in word:
        if x == letter :
            count = count + 1
    return count, letter

print(fruit, "tem", conta("n",fruit))
'''
'''
print(fruit)
print(fruit[39:41])
fruta=fruit[39:41]
print(fruta)
print(fruit.replace(fruta, "78"))
'''
print(fruit)
#stra = fruit
posn = 39
nc = '78'

fruit = fruit[:posn] + nc + fruit[posn+2:]
print(fruit)