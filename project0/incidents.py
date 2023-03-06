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

def extractpdflocal(data):
    """use to pull local copy of pdf incident summary"""
    reader = PdfReader(data)
    return reader

def extractpdf(data):
    """use when pulling live copy of pdf incident summary direct from normanPD"""
    #for when we switch back to urllib
    processed_data = io.BytesIO(data)
    reader = PdfReader(processed_data)
    return reader
  
def jt(x):
    return ''.join(x).strip()

def parsepdf(data):
    #json_incidents = {'incidents':[]}
    parsed_data = []
    for p in data.pages:
        page = p.extract_text()
        re_date = re.findall(r'[12]\/[1-3]\d\/202[0-3] \d\d?:\d\d',page)
        re_no = re.findall(r'202[0-3]-\d{8}',page)
        re_loc = re.findall(r'(?<=[\d]{4}\-[\d]{8})[A-Z0-9 \/\n;\-\.\']*[A-Z02-9](?= [^N]..[^h])',page)
        re_nat = re.findall(r'(?<=[A-Z\d] )(MVA )?(911 )?([A-Z][a-z]+.*)(?= [EO\d])',page)
        re_ori = re.findall(r'(?<=[A-Za-z] )EMSSTAT|(OK0)?14\d*(?=\n|$)',page)
        for x,y,z,a,b in zip(re_date, re_no, re_loc, re_nat, re_ori):
            parsed_data.append([x,y,jt(z),jt(a),jt(b)])
    return parsed_data

def database(parsed_data):
    conn = sqlite3.connect('norman.db')
    curs = conn.cursor()
    curs.execute("DROP TABLE IF EXISTS INCIDENTS")
    curs.execute( """
    CREATE TABLE INCIDENTS (
    incident_time TEXT
    ,incident_number TEXT
    ,incident_location TEXT
    ,nature TEXT
    ,incident_ori TEXT
    );
    """)
    for x in parsed_data:
        t = (x[0],x[1],x[2],x[3],x[4])
        curs.execute("INSERT INTO INCIDENTS VALUES (?,?,?,?,?)",t)
        conn.commit()
    conn.close()

def digest():
    conn = sqlite3.connect('norman.db')
    curs = conn.cursor()
    select_all = "SELECT incident_time, incident_location FROM INCIDENTS;"
    count_nat = "SELECT nature,COUNT(nature) FROM INCIDENTS GROUP BY nature ORDER BY COUNT(nature) DESC, nature;"
    rows = curs.execute(count_nat).fetchall()
    result = []
    for row in rows:
        result.append([row[0],row[1]])
        #summing results in right column to facilitate testing
        #sum += int(row[1])
    conn.close()
    return result
