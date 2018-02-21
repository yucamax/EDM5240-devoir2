#coding:utf-8

### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

#importer le fichier csv

import csv
import datetime

### Je rajuste le nom du fichier pour tester ton code

fichier="../grants.csv"

f1=open(fichier)
lignes = csv.reader(f1)
next(lignes)

### Très bien: tu as vu qu'il y avait plusieurs programmes différents dans le Fonds

#isoler les lignes contenant le nom d'un des trois programmes chapeauté par le Fonds du Canada pour les périodiques

n=0

for ligne in lignes:
	### Je déplace ton compteur dans les conditions afin de ne compter que les subventions du Fonds
	# n+=1
	if any("Aide aux éditeurs" in s for s in ligne):
		n += 1
		### J'ajoute «n» dans tes trois «print» pour vérifier le nombre de subventions repérées
		print(ligne,n)
	elif any("Innovation commerciale" in s for s in ligne):
		n += 1
		print(ligne,n)
	elif any("Initiatives collectives" in s for s in ligne):
		n += 1
		print(ligne,n)

### Pourquoi te donner tout ce mal?
### Il suffisait de chercher «Fonds du Canada pour les périodiques» ou «FCP» dans un même «if», double, avec un «or»:
### «if "Fonds du Canada pour les périodiques" in ligne[17] or "FCP -" in ligne[17]:»

#Extraire les années de chacune des lignes

f1=open(fichier)
lignes = csv.reader(f1)
next(lignes)

for ligne in lignes:
	year = (ligne[13][0:4])

	if any("Aide aux éditeurs" in s for s in ligne):
		print(year)
	elif any("Innovation commerciale" in s for s in ligne):
		print(year)
	elif any("Initiatives collectives" in s for s in ligne):
		print(year)

#l'impression totale donnera la liste contenant les différents programmes du Fonds du Canada pour les périodiques
#Dans un deuxième temps, seules les années (et non les dates entières) seront imprimées

### Tu vas bien chercher les années avec la bonne formule
### Mais il aurait été préférable d'imprimer l'année en même temps que le reste de la ligne
### Pour cela, il fallait faire «ligne.append(year)»
