from pymongo import MongoClient

# Replace with your connection details
client = MongoClient("mongodb://silentadmin:silentPass123@127.0.0.1:27017")

db = client["silentmon"]
collection_name = "users"

# Fetch all documents
documents = list(db[collection_name].find())

# Print retrieved documents
for document in documents:
    print(document)

# Close the connection (optional)
client.close()




mongo_client = MongoClient("mongodb://silentadmin:silentPass123@localhost:27017")
mongo_silentdb = mongo_client["silentmon"]
mongo_silentcoll = mongo_silentdb["users"]

documents = list(mongo_silentcoll.find())

# Print retrieved documents
for document in documents:
    print(document)

mongo_client.close()