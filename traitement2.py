# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv, os, glob
import pymysql.cursors
from motsvides import rien
import nltk
from nltk.tokenize import word_tokenize
import treetaggerwrapper

rep = input("On veut mots seuls (1), 2-grams (2) ou 3-grams (3)?")

tag = treetaggerwrapper.TreeTagger(TAGLANG='fr')

connection = pymysql.connect(host='localhost',
	user='root',
	password="",
	db='facebook',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
	sql = "SELECT * FROM posts"
	cursor.execute(sql)
	posts = cursor.fetchall()

nb = 0
t = 0
m = 0
liste = []

for post in posts:
	# print(post)
	nb += 1
	# print(nb)
	engagement = post["partages"] + post["reactions"] + post["commentaires"] + post["likes_commentaires"] + post["commentaires_commentaires"]
	# print(engagement)
	if engagement != 0:
		textes = [post["message"],post["nom"],post["description"]]
		for item in textes:
			if item != "?" and "Timeline" not in item and "cover" not in item:
				t += 1
				# print(t,nb,item)
				mots = word_tokenize(item)

## Pour compter mots pondérés

				if rep == "1":
					fichierOUT = "facebook-mots-medias.csv"
					for mot in mots:
						mot = mot.lower()
						if mot not in rien:
							if mot.isalpha():
								lemme = tag.tag_text(mot)
								lemme = lemme[0].split("\t")
								if mot != "http" or mot != "https":
									m += 1
									print(mot,lemme[2],engagement,m,t,nb)
									ajout = [lemme[2],engagement]

									ying = open(fichierOUT, "a")
									yang = csv.writer(ying)
									yang.writerow(ajout)

### Pour compter 2-grams pondérés

				elif rep == "2":
					fichierOUT = "facebook-bigrams-medias.csv"
					i = 0
					for mot in mots[:-1]:
						mot = mot.lower()
						if mot.isalpha():
							if len(mot) > 1:
								i += 1
								if mot != mots[i].lower():
									if mot not in rien or mots[i].lower() not in rien:
										if "." not in mot and "," not in mot and "-" not in mot and "’" not in mot and "!" not in mot and ":" not in mot and "." not in mots[i] and "," not in mots[i] and "-" not in mots[i] and "’" not in mots[i] and "!" not in mots[i] and ":" not in mots[i]:
											bigram = "{} {}".format(mot,mots[i])
											# print(nb,bigram)
											ajout = [bigram, engagement]
											# liste.append(bigram)
											print(ajout,nb)

											ying = open(fichierOUT, "a")
											yang = csv.writer(ying)
											yang.writerow(ajout)

### Pour compter 3-grams pondérés

				elif rep == "3":
					fichierOUT = "facebook-trigrams-medias.csv"
					i = 0
					for mot in mots[:-2]:
						mot = mot.lower()
						if mot.isalpha():
							if len(mot) > 1:
								i += 1
								if mot != mots[i].lower() and mots[i].lower() != mots[i+1].lower() and mot != mots[i+1].lower():
									if (mot not in rien or mots[i].lower() not in rien) and (mots[i].lower() not in rien or mots[i+1].lower() not in rien):
										trigram = "{} {} {}".format(mot,mots[i].lower(),mots[i+1].lower())
										ajout = [trigram, engagement]
										# liste.append(bigram)
										print(ajout,nb)

										ying = open(fichierOUT, "a")
										yang = csv.writer(ying)
										yang.writerow(ajout)

				else:
					print("Mauvaise réponse")
