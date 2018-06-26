![](http://comsante.uqam.ca/wp-content/uploads/2016/08/bandeau-comsante2-01.jpg)

# fb-sante
### Pourquoi on partage/aime/commente des contenus santé sur Facebook?

Documents relatifs à une présentation faite dans le cadre de l'[École d'été «S'informer dans un monde de fausses informations» (juin 2018)](https://comsante.uqam.ca/ecole-dete-sinformer-dans-un-monde-de-fausses-informations-produire-et-interpreter-des-contenus-dans-le-nouvel-ecosysteme-informationnel-du-26-au-28-juin-2018/).<br>Étude sur les publications de 69 pages Facebook relatives à la santé entre janv. 2013 et mai 2018.

### Code

Quatre fichiers python dans l'ordre:

* **[extraction.py](extraction.py)** -> script permettant d'extraire les publications (*posts*) de la liste de pages Facebook se trouvant dans **[sources.csv](sources.csv)**.
* **[traitement1.py](traitement1.py)** -> script effectuant un premier traitement des publications, comptant le nombre d'emojis, de mots, de n-grams *non-pondérés*.
* **[traitement2.py](traitement2.py)** -> script effectuant un second traitement des publications, comptant le nombre de mots, de n-grams *pondérés* en fonction de l'engagement suscité par le post dans lequel ils se trouvent.
* **[motsvides.py](motsvides.py)** -> simple variable comprenant les mots vides (*stop words*) exclus du décompte des mots dans les premier et second traitements

### Données

* **[sources.csv](sources.csv)** -> liste des 69 pages Facebook utilisées dans le cadre de cette étude

* **Fichiers des publications** (séparés par année, parce que le fichier complet est trop volumineux pour Github)

  * **[posts-2013-2014.csv](posts-2013-2014.csv)** -> 26&nbsp;747 publications en 2013 et 2014
  * **[posts-2015.csv](posts-2015.csv)** -> 18&nbsp;432 publications en 2015
  * **[posts-2016.csv](posts-2016.csv)** -> 22&nbsp;177 publications en 2016
  * **[posts-2017.csv](posts-2017.csv)** -> 25&nbsp;820 publications en 2017
  * **[posts-2018.csv](posts-2018.csv)** -> 25&nbsp;053 publications dans les premiers mois de 2018
