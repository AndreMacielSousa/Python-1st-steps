#Comentario simples
'''
Comentario multi linhas
'''
msg= "ola mundo\nSimulador de ciclo"
print(msg)
#ciClo While
n=5
while n>0 :
    print(n)  
    n = n - 1
print('Boom')
# calculos e prioridades
x = 2
x = 3.9 * x * (1-x)
print(x)
# Divisão sempre float
width = 15
height = 12
print(height/3)
# Variancoes de somatorio 
x = 5
x += 5
print(x)
# funcao tipo
print(x, "é do tipo", type (x),"\n")
# Input
name = input(" Qual o teu nome? ")
print ("ola", name, "\n")
# Converter Input
inp = input("Europe Floor")
usf = int(inp) + 1
print ("US Floor", usf)
usf = float(inp) + 1
print ("US Floor", usf)