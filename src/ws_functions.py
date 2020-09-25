import requests
import bs4
import re
import itertools
import time
import json

#Function to get users from web scraping GitHub
def getUsers(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    users = re.findall("@\w+\S\w\w*", str(soup))
    users = list(set(users))
    unwanted_users =['@ferrero-felipe', '@WHYTEWYLL', '@agalvezcorell', '@github', '@ironhack-datalabs']
    for i in unwanted_users:
        if i in users:
            users.remove(i)
    dic_users = { i : users[i] for i in range(0, len(users) ) }
    dic_users = {v: k for k, v in dic_users.items()}
    return dic_users

#Function to split dictionaries into n chunks dictionaries
def split_dict(input_dict, chunks=28):
    "Splits dict by keys. Returns a list of dictionaries."
    # prep with empty dicts
    return_list = [dict() for idx in range(chunks)]
    idx = 0
    for k,v in input_dict.items():
        return_list[idx][k] = v
        if idx < chunks-1:  # indexes start at 0
            idx += 1
        else:
            idx = 0
    return return_list