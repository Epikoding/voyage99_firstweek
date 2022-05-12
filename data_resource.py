from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.feuh6.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca) #minsu
# client = MongoClient('mongodb+srv://test:sparta@sparta.eacl0.mongodb.net/sparta?retryWrites=true&w=majority', tlsCAFile=ca) #동재

db = client.dbfirstweek

# 비밀 키 설정
SECRET_KEY = 'SPARTA'