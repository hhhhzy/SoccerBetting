import pandas as pd
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import os
import time


def scoresfixtures(link,ids):
    '''
    Description: This Class picks all the games that had in one season and combinate all links to one especific list
    
    Inputs:
        - link: The link of the main page that have all season games desired.
        - ids: The ID of the championship table
        
    Outputs:
        - especific list that has all the links os all matches of the season
    
    
    '''
    req = requests.get(link)
    if req.status_code == 200:
        content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    tb = soup.find(id=ids)

    s1= []
    s2= []
    for i in tb.find_all("a"):
            s1.append(str(i))
            s2.append(str(i.get_text('href')))


    # Calling DataFrame constructor after zipping 
    # both lists, with columns specified 
    di = pd.DataFrame(list(zip(s1, s2)), 
                   columns =['Codes', 'ID']) 

    s4=[]
    for i in di["Codes"]:
        i = i.replace('<a href="','')
        i = i.replace('</a>','')
        s4.append(str(i))


    s5 = []

    for i in di['Codes']:
        if "matches" in i:
            s5.append(str(i))
        else:
            s5.append(0)

    s6 = []
    for i in di["Codes"]:
        if '<a href="/en/squads/' in i:
            i = i.replace('<a href="/en/squads/','')
            i = i[0:8]
            s6.append(str(i))
        else:
            s6.append(0)        

    # Calling DataFrame constructor after zipping 
    # both lists, with columns specified 
    da = pd.DataFrame(list(zip(s1, s2,s4,s5,s6)), 
                   columns =['CODES', 'ID','URL_FINAL','PARTIDAS_2019',"TEAM_CODE"])        

    s9 = []
    for i in da["URL_FINAL"]:
        if 'Match Report' in i:
            s9.append(str(i))
        else:
            pass
    return s9
