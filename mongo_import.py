from src.api_functions import getRequests, getDataDict
from src.ws_functions import getUsers, split_dict
from src.import_functions import Import_to_mongoDB, import_users


npages = getRequests("/repos/ironhack-datalabs/datamad0820/pulls",query_params={'state': 'all', 'page' : 1, "per_page":100})[0]['number']

list_pulls = getDataDict(npages)

Import_to_mongoDB(list_pulls)

scrap_url = 'https://github.com/ironhack-datalabs/datamad0820/network/members'

users = split_dict(getUsers(scrap_url))

import_users(users)