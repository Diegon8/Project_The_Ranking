from pymongo import MongoClient

#Function to import all pull dictionaries to MongoDB
def Import_to_mongoDB(lista):
    """Upload the info extractred from github to mongodb"""
    client = MongoClient(port=27017)
    db=client.RankingDB
    for x in range(0,len(lista)):
        result = db.pulls.insert_one(lista[x])
    print(f'finished adding {len(lista)} pull requests')


#Function to import all users to MongoDB
def import_users(lista):
    client = MongoClient(port=27017)
    db=client.RankingDB
    for x in range(0,len(lista)):
        result = db.users.insert_one(lista[x])
    print(f'finished adding {len(lista)} users')