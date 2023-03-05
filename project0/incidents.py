import json
import io
import os
import re
import sqlite3
import urllib.request
from pypdf import PdfReader

def getpdf(url): 
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    #print("getpdf works")
    return data

def json_dict(date,no):
    #json_dict = {"date":date,"incident_no":no,"location":loc,"nature":nat,"incident_ori":ori}
    json_dict = {"date":date,"incident_no":no}
    return json_dict

def extractpdflocal(data):
    """use to pull local copy of pdf incident summary"""
    reader = PdfReader(data)
    return reader
    #for p in reader.pages:
        #print(p.extract_text())


def extractpdf(data):
    """use when pulling live copy of pdf incident summary direct from normanPD"""
    #for when we switch back to urllib
    processed_data = io.BytesIO(data)
    reader = PdfReader(processed_data)
    return reader
    json_incidents = {'incidents':[]}
    #key_list = ['date', 'incident_no', 'location', 'nature', 'incident_ori']
    
    #re_list = [re_date, re_incident_no, re_location, re_nature, re_incident_ori] 
    #for p in reader.pages:
        #print(p.extract_text())

    #print(reader.pages[25].extract_text()[0:300])
    #print(len(reader.pages))
    #print(reader)

def parsepdf(data):
    json_incidents = {'incidents':[]}
    for p in data.pages:
        page = p.extract_text()
        re_date = re.findall(r'[12]\/[1-3]\d\/202[0-3] \d\d?:\d\d',page)
        re_no = re.findall(r'202[0-3]-\d{8}',page)
        #print(page)
        for x,y in zip(re_date, re_no):
            print(x,' | ',y)
            #json_incidents['incidents'].append(json_dict(re_date[x],re_no[x]))
    #json_object = json.dumps(json_incidents,indent = 4)
    #print(json_object)
    #print('re_date:',len(re_date))
    #print(re_date))

def database():
    pass

def insertdata(db, incidents):
    pass

def incident_digets():
    pass

def checker():
    print("the test works")
