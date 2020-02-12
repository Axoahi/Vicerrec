import pymongo
from bson.objectid import ObjectId

#Conexion a mongoDB con BD y coleccion
uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(uri)
database = client['vice']
collection = database['estadisticas']

########CRUD de la BD con la coleccion estadisticas #################
# def crearEstadisticas(estadistica):
# 	_id = collection.insert_one(estadistica).inserted_id
# 	return _id

def listaEstadisticas():
	listado = collection.find({})
	return listado[0]

def findEstadisticasByKey(key):
	estadistica = collection.find( {key:{"$exists": True}} )

	return estadistica

def actualizarEstadistica(key):
	item = collection.find_and_modify(query={"tipo":"documentos procesados"}, update={"$inc": {key: 1}}, upsert=False)
	if(item != ""):
		return True
	else:
		return False

def borrarEstadistica(id):
	collection.delete_one({"_id": ObjectId(id)})
	print("Item borrado")




