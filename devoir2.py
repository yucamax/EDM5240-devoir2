#coding:utf-8

#importer le fichier csv

import csv
import datetime

fichier="grants.csv"

f1=open(fichier)
lignes = csv.reader(f1)
next(lignes)

#isoler les lignes contenant le nom d'un des trois programmes chapeauté par le Fonds du Canada pour les périodiques

n=0

for ligne in lignes:
	n+=1
	if any("Aide aux éditeurs" in s for s in ligne):
		print(ligne)
	elif any("Innovation commerciale" in s for s in ligne):
		print(ligne)
	elif any("Initiatives collectives" in s for s in ligne):
		print(ligne)

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
