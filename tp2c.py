#Benjamin Sigouin, 404
#TP2

print("Hello World!")

nombre = int(input("Combien de rangée d'étoiles voulez-vous?"))
for i in range(nombre +1, 0, -1):
    print("*"*i)