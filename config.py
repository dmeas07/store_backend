import pymongo
import certifi

con_str = "mongodb+srv://daravy:74108520@cluster0.yju10tk.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("Coffee")

me = {
    "first_name": "Daravy",
    "last_name": "Meas",
    "age": 33,
}


def hello():
    print("Hello There")
