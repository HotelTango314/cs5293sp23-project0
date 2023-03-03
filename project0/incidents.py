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
    print("getpdf works")
    return data

def json_dict(date,no,loc,nat,ori):
    json_dict = {"date":date,"incident_no":no,"location":loc,"nature":nat,"incident_ori":ori}
    return json_dict

def extractpdf(data):
    processed_data = io.BytesIO(data)
    reader = PdfReader(processed_data)
    json_incidents = {'incidents':[]}
    key_list = ['date', 'incident_no', 'location', 'nature', 'incident_ori']
    re_date = re.compile(r'[12]\/[1-3]\d\/202[0-3]\s\d\d:\d\d')
    re_incident_no = re.compile(r'/202[0-3]-\d{8}/gm')
    re_location = re.compile(r'.2.')
    re_nature = re.compile(r'')
    re_incident_ori = re.compile(r'.2.')
    re_list = [re_date, re_incident_no, re_location, re_nature, re_incident_ori]
    for p in reader.pages:
       # print(p.extract_text())
       page = p.extract_text()
       for q in re_list:

    #print(reader.pages[25].extract_text()[0:300])
    #print(len(reader.pages))
    #print(reader)
    


def database():
    pass

def insertdata(db, incidents):
    pass

def incident_digets():
    pass

def checker():
    print("the test works")
