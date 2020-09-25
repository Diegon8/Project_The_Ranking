from src.api_functions import getRequests, getDataDict
from src.ws_functions import getUsers, split_dict
from src.import_functions import Import_to_mongoDB, import_users

#Number of pages of pull requests
npages = getRequests("/repos/ironhack-datalabs/datamad0820/pulls",query_params={'state': 'all', 'page' : 1, "per_page":100})[0]['number']

#Create list of all pulls
list_pulls = getDataDict(npages)

#Import list of pulls to MongoDB with all its data
Import_to_mongoDB(list_pulls)

#Scrap for datamad0820 students/users
scrap_url = 'https://github.com/ironhack-datalabs/datamad0820/network/members'

users = split_dict(getUsers(scrap_url))

#Import users to MongoDB
import_users(users)