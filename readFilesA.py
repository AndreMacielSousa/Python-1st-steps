#File Processing (r - READ / W - write)
xfile = open("texto.txt","r")
for line in xfile:
    print(line)
print("\n***************************")

#Couting lines
xfile = open("texto.txt")
count = 0
for line in xfile:
    count = count +1
print("Linhas = ", count)
print("\n***************************")

#Read de whole file into a single string
xfile = open("texto.txt")
inp = xfile.read()
print(len(inp))
print(inp[:20])
print("\n***************************")

#Search through a file
xfile = open("texto.txt")
for line in xfile:
    if line.startswith("De"):
        print(line)
print("\n***************************")

#Remover \n do final das linhas
xfile = open("texto.txt")
for line in xfile:
    line = line.rstrip()  # aqui
    if line.startswith("De"):
        print(line)
print("\n***************************")

#Skipping with continue
xfile = open("texto.txt")
for line in xfile:
    line = line.rstrip()  
    if not line.startswith("De"): # aqui
        continue                  # aqui
    print(line)
print("\n***************************")

#Using in to select lines
xfile = open("texto.txt")
for line in xfile:
    line = line.rstrip()  
    if not "De" in line: # aqui
        continue                 
    print(line)
print("\n**in************************")

#Prompt for File name and Bad Names
fname = input("Enter the file name: ")
try:
    xfile = open(fname)
except:
    print("File cannot be open: ", fname)
    quit()
    #Skipping with continue
xfile = open("texto.txt")
for line in xfile:
    line = line.rstrip()  
    if not line.startswith("C"): # aqui
        continue                  # aqui
    print(line)
print("\n***************************")


