# Demander des nom de personnes
# Boucles infinie, sort quand le nom est vide == "" -> break
# À la fin affichez tout les noms


noms = []
while True:
    nom = input("Nom de la personne: ")
    if nom == "":
        break
    noms.append(nom)
print()
print("Nom des personnes")
noms.sort()  # tiage with ordre alphabétique
for nom in noms:
    print("  " + nom)
