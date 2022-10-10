#FIND (devolve a posicao) / -1 quando nao existe
word = "bananana"
i = word.find("na")
print(i)

#slicing Strins
s = "Monty Phyton"
print(s[0:4])
print(s[6:20])
print(s[:4])
print(s[6:])
print(s[:])

#String Concatenation
a = "\nOla "
b = a + s
print(b)

#Using IN as logical operator
fruit = "banana"
print("n" in fruit)
print("N" in fruit)
print("nan" in fruit)

#String lower()
#lstrip() remove espaço esquerda
#rstrip() remove espaço direita
#strip() remove espacos inciais a esquerda e direita
greet = " Ola Andre "
print(greet.strip().lower())

#String Methods
print("\n",dir(greet),"\n")

#Search and Replace
print(greet.replace("Andre", "Tomas"))
print(greet.replace(greet[0:4], "Hello"))

#Prefixes
word = "CZZZE"
print(word.startswith("C"))

#Parsing and Extracting
data = "From sousa@andremaciel.pt Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos)
sppos = data.find(" ",atpos) #procura o espaço depois do @
print(sppos)
host = data[atpos+1 : sppos]
print(host)