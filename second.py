#identacao condicional
x=0
y=10
if 0 == x:
    if y == 10:
        print("Yes")

if y > 0: print("Yes")

#Condicional for 
for i in range(-1,5):
    print("\ni'm ",i)
    if i > 2:
        print("Bigger then 2")
    print("Done wiht i", i)
print("All done\n")

# If Then Else
x=4
if x > 2:
    print("Bigger")
else:
    print("Smaller")
print("End\n")

#ElIf MultiWAY - a primeira ocorrencia
if x < 2:
    print("Small")
elif x < 5:
    print("Medium")
elif x < 10:
    print("Large")
else:
    print("Bigger")
print("End\n")

#Try/except
temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
except:
    fahr = 5
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

num = input("\nEnter a number: ")
try:
    ival= int(num)
except:
    ival = -1
if ival > 0 : print ("obrigado")
else: print("Não é um numero")