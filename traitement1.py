import csv, os, glob, emoji
import pymysql.cursors
from motsvides import rien
import nltk
from nltk.tokenize import word_tokenize
import treetaggerwrapper

rep = input("On veut emojis (0), mots seuls (1), bigrammes (2) ou trigrammes (3)?")

tag = treetaggerwrapper.TreeTagger(TAGLANG='fr')

connection = pymysql.connect(host='localhost',
	user='root',
	password="1234567",
	db='fb_sante',
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

### Pour compter emojis

				if rep == "0":
					letype = "emojis"
					for mot in mots:
						if mot in emoji.UNICODE_EMOJI:
							print(mot)
							liste.append(mot)

### Pour compter mots lemmatisés

				elif rep == "1":
					letype = "mots"
					for mot in mots:
						mot = mot.lower()
						if mot not in rien:
							if mot.isalpha():
								lemme = tag.tag_text(mot)
								lemme = lemme[0].split("\t")
								m += 1
								print(mot,lemme[2],t,nb,m)
								liste.append(lemme[2])

### Pour compter 2-grams

				elif rep == "2":
					letype = "bigrams"
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
											print(nb,bigram)
											liste.append(bigram)

### Pour compter 3-grams

				elif rep == "3":
					letype = "trigrammes"
					i = 0
					for mot in mots[:-2]:
						mot = mot.lower()
						if mot.isalpha():
							if len(mot) > 1:
								i += 1
								if mot != mots[i].lower() and mots[i].lower() != mots[i+1].lower() and mot != mots[i+1].lower():
									if (mot not in rien or mots[i].lower() not in rien) and (mots[i].lower() not in rien or mots[i+1].lower() not in rien):
										trigram = "{} {} {}".format(mot,mots[i].lower(),mots[i+1].lower())
										print(nb,trigram)
										liste.append(trigram)

				else:
					print("Mauvaise réponse")

print("$"*40)

distFreq = nltk.FreqDist(liste)
for m, frequence in distFreq.most_common(200):
	print('{} ->\t {}'.format(m, frequence))
