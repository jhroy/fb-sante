# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv, requests, json
from datetime import datetime
from pytz import timezone

heureEst = timezone("Canada/Eastern")

fichier1 = "sources-pages-sante-2.csv"
# fichier1 = "ajouts.csv"
jeton = "EAACE[...]" #masqué pour raisons de confidentialité

f1 = open(fichier1)
pages = csv.reader(f1)
next(pages)

def fb(post,publications):
	date = datetime.strptime(post["created_time"],"%Y-%m-%dT%H:%M:%S%z")
	if date.year in [2013,2014,2015,2016,2017,2018]:
		# print(post)
		p = []
		p.append(page[1])
		p.append(page[2])
		p.append(publications)
		p.append(date)
		dateQC = date.astimezone(heureEst)
		p.append(datetime.strftime(dateQC, "%Y-%m-%dT%H:%M:%S%z"))
		p.append(post["id"])
		try:
			p.append(post["message"])
		except:
			p.append("?")
		try:
			p.append(post["name"])
		except:
			p.append("?")
		try:
			p.append(post["description"])
		except:
			p.append("?")
		try:
			p.append(post["caption"])
		except:
			p.append("?")
		try:
			p.append(post["story"])
		except:
			p.append("?")
		try:
			p.append(post["source"])
		except:
			p.append("?")
		try:
			p.append(post["link"])
		except:
			p.append("?")
		try:
			p.append(post["status_type"])
		except:
			p.append("?")
		try:
			p.append(post["type"])
		except:
			p.append("?")

		try:
			p.append(post["shares"]["count"])
		except:
			p.append(0)

		p.append(post["reactions"]["summary"]["total_count"])
		p.append(post["comments"]["summary"]["total_count"])

		reponses = 0
		comment_likes = 0
		for com in post["comments"]["data"]:
			reponses += com["comment_count"]
			comment_likes += com["like_count"]
		p.append(reponses)
		p.append(comment_likes)

		try:
			engagement = post["shares"]["count"] + post["reactions"]["summary"]["total_count"] + post["comments"]["summary"]["total_count"] + reponses + comment_likes
		except:
			engagement = post["reactions"]["summary"]["total_count"] + post["comments"]["summary"]["total_count"] + reponses + comment_likes
		p.append(engagement)

		print(p)

		tintin = open(fichier2,"a")
		milou = csv.writer(tintin)
		milou.writerow(p)

for page in pages:

	# print(page)
	fichier2 = "posts/posts-{}.csv".format(page[0])
	print("On extrait {}".format(page[1]))

	publications = 0

	req = "https://graph.facebook.com/v3.0/{}?fields=posts.limit(100)%7Bmessage%2Cdescription%2Ccaption%2Clink%2Cname%2Cstatus_type%2Csource%2Cstory%2Ccreated_time%2Ctype%2Cshares%2Ccomments.summary(true).limit(100)%7Bcomment_count,like_count%7D%2Creactions.summary(1)%7D&access_token={}".format(page[2],jeton)
	posts = requests.get(req).json()
	# print(posts["posts"]["data"])
	print(len(posts["posts"]["data"]))
	# print(posts)

	for post in posts["posts"]["data"]:
		publications += 1
		fb(post,publications)

	if len(posts["posts"]["data"]) > 99:
		next = posts["posts"]["paging"]["next"]
		# print(next)
		print("*"*80)
		posts = requests.get(next).json()

		while(True):
			try:
				for post in posts["data"]:
					publications += 1
					fb(post,publications)

				posts = requests.get(posts["paging"]["next"]).json()

			except KeyError:
				break
