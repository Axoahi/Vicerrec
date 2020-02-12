import pymongo
from bson.objectid import ObjectId

#Conexion a mongoDB con BD y coleccion
uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(uri)
database = client['vice']
collection = database['acepciones']

########CRUD de la BD con la coleccion Acepciones#################
def crearAcepcion(acepcion):
	_id = collection.insert_one(acepcion).inserted_id
	return _id

def listaAcepciones():
	listado = collection.find({})
	return listado[0]

def findAcepcionesByUser(user):
	acepcion = collection.find({'user': user})
	return acepcion[0]

def actualizarAcepcion(user, acepcion):
	id = collection.replace_one({'user': user},acepcion)
	return id

def borrarAcepcion(id):
	id = collection.delete_one({"_id": ObjectId(id)})
	print("Item borrado")




