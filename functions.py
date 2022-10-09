#Stored and reused steps
def thing():
    print("Ola")
    print("Amigo")

thing()
print("qqr coisa")
thing()

#Parametros
def greet(lang):
    if lang == "es": print("Hola")
    elif lang == "fr": print("Bonjour")
    else: print("Hello")

print("\nparametros")
greet("lol")
greet("es")
greet("fr")

#Return Values
def greet(lang):
    if lang == "es": return "Hola"
    elif lang == "fr": return "Bonjour"
    else: return"Hello"

print("\nreturn")
print(greet("fr"),"Francoise")
print(greet("es"),"Zorro")
print(greet("xp"),"Michael")