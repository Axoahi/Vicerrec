import pymongo
from bson.objectid import ObjectId

#Conexion a mongoDB con BD y coleccion
uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(uri)
database = client['vice']
collection = database['estudio']

########CRUD de la BD con la coleccion ESTUDIO#################
def crearEstudio(estudio):
	_id = collection.insert_one(estudio).inserted_id
	return _id

def listaEstudios():
	listado = collection.find({})
	return listado

def findEstudio(id):
	estudio = collection.find({'_id': ObjectId(id)})
	return estudio[0]

def actualizarEstudio(estudio):
	collection.replace_one({'_id': ObjectId(estudio['id'])},estudio)
	return id

def borrarEstudio(id):
	collection.delete_one({"_id": ObjectId(id)})
	print("Item borrado")




