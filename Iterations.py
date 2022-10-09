# Exemplo While Loop com Break
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1

# Exemplo While Loop com Continue

while True:
    line = input("> ")
    if line[0] == "#" : continue
    if line == "done" : break
    print(line)
print("Bye")


