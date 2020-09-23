from src.Functions import getRequests, getDataDict, Import_to_mongoDB

npages = getRequests("/repos/ironhack-datalabs/datamad0820/pulls",query_params={'state': 'all', 'page' : 1, "per_page":100})[0]['number']

list_pulls = getDataDict(npages)

Import_to_mongoDB(list_pulls)