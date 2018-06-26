![](http://comsante.uqam.ca/wp-content/uploads/2016/08/bandeau-comsante2-01.jpg)

# fb-sante
### Pourquoi on partage/aime/commente des contenus santé sur Facebook?

Documents relatifs à une présentation faite dans le cadre de l'École d'été «S'informer dans un monde de fausses informations» (juin 2018).

### Code

Quatre fichiers python dans l'ordre:

- **[extraction.py](extraction.py)** -> script permettant d'extraire les publications (*posts*) de la liste de pages Facebook se trouvant dans **[sources.csv](sources.csv)**.
- **[traitement1.py](traitement1.py)** -> script effectuant un premier traitement des publications, comptant le nombre d'emojis, de mots, de n-grams *non-pondérés*.
- **[traitement2.py](traitement2.py)** -> script effectuant un second traitement des publications, comptant le nombre de mots, de n-grams *pondérés* en fonction de l'engagement suscité par le post dans lequel ils se trouvent.
- **[motsvides.py](motsvides.py)** -> simple variable comprenant les mots vides (*stop words*) exclus du décompte des mots dans les premier et second traitements
