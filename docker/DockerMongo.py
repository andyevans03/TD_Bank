import pymongo
# Import de la classe MongoClient qui nous permettra de nous connecter a la base de donnees MongoDB
from pymongo import MongoClient

client = MongoClient(host="mongodb")

# Acces a la base de donnees "NOM_BASE_DE_DONNEES"
db = client["NOM_BASE_DE_DONNEES"]

# Acces a la collection "NOM_COLLECTION"
col = db["NOM_COLLECTION"]

# Ajout d'un 'fruit' dans la collection
fruit = {
        "nom": "banane",
        "couleur": "jaune"
}
res = col.insert_one(fruit)

# Verification de l'ajout
print(f'Le fruit {res.inserted_id} a bien ete cree')

# Localise et affiche le fruit
col.find_one()