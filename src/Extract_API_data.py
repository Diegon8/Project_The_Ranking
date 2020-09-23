import os
from dotenv import load_dotenv
load_dotenv()
import json
import requests
import re
import math
import itertools


#Function that extracts gross data from GitHub API
def getRequests(endpoint, token=os.getenv("apikey"), query_params={}):

    baseUrl = "https://api.github.com"
    url = f"{baseUrl}{endpoint}"

    headers = {
        "Authorization": f"token {token}"
    }

    res = requests.get(url, params=query_params, headers=headers)

    data = res.json()

    if res.status_code != 200:
        raise ValueError(f'Invalid github api call: {data["message"]}')

    return data


#Formula to process gross data into Dictionary with only needed info
def extractWantedData(data):

    """Create a dictionary with the selected information received from the github api"""
    dictionary=[]
    for x in range(0,len(data)):
        try:
            name={'number':data[x]['number'],
            'title':re.match('\[(.*?)\]',data[x]['title'],re.IGNORECASE).group(1).replace('-',' '),
            'user':data[x]['user']['login'],
            'state':data[x]['state'],
            'created_at':data[x]['created_at'],
            'updated_at':data[x]['updated_at'],
            'closed_at':data[x]['closed_at'],
            'html_url':data[x]['html_url'],
            'meme':'no'
            }
            dictionary.append(name)
    
        except:
            name={'number':data[x]['number'],
            'title':re.match('\[(.*?)\]',data[x-1]['title'],re.IGNORECASE).group(1).replace('-',' '),
            'user':data[x]['user']['login'],
            'state':data[x]['state'],
            'created_at':data[x]['created_at'],
            'updated_at':data[x]['updated_at'],
            'closed_at':data[x]['closed_at'],
            'html_url':data[x]['html_url'],
            'meme':'no'
            }
            dictionary.append(name)
            
    return dictionary


#Variable containing number of pages
npages = getRequests("/repos/ironhack-datalabs/datamad0820/pulls",query_params={'state': 'all', 'page' : 1, "per_page":100})[0]['number']


#Function that apllies processing formula to all pulls from all pages
def getDataDict(npages):
    """Get the information from all the github issues pages from a selected repository"""
    pulls = []
    for i in range(1, math.ceil(npages/100) + 1):
        pulls.append(extractWantedData(getRequests("/repos/ironhack-datalabs/datamad0820/pulls",query_params={'state': 'all', 'page' : i, "per_page":100})))
    clean_data = list(itertools.chain.from_iterable(pulls))
    return clean_data