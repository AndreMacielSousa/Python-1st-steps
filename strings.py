#Comprimento
fruit = input("Escolha uma Fruta: ")
print("Comprimento ", fruit," ", len(fruit))

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