from project0 import incidents
import os
import sqlite3

def test_getpdf(url='https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-27_daily_incident_summary.pdf'):
    tester = incidents.getpdf(url)
    #print(tester[0:8])
    assert tester[0:8] == b'%PDF-1.5'

def test_extractpdf(url = 'https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-27_daily_incident_summary.pdf'):
    tester = incidents.getpdf(url)
    assert incidents.extractpdf(tester).pdf_header == '%PDF-1.5'

def test_extractpdflocal(filename = 'docs/feb27_incidents.pdf'):
    tester = incidents.extractpdflocal(filename)
    #print(tester.pdf_header)
    assert tester.pdf_header == '%PDF-1.5'

def test_jt(x = [' ',' ','h','e','l','l','o',' ',' ']):
    tester = incidents.jt(x)
    assert tester == 'hello'

def test_parsepdf(filename = 'docs/feb27_incidents.pdf'):
    tester = incidents.extractpdflocal(filename)
    x = len(incidents.parsepdf(tester))
    y = len(incidents.parsepdf(tester)[0])
    print(x)
    print(y)
    assert x == 495 and y == 5

def test_database(filename = 'docs/feb27_incidents.pdf'):
    tester = incidents.extractpdflocal(filename)
    parsed = incidents.parsepdf(tester)
    incidents.database(parsed)
    conn = sqlite3.connect('norman.db')
    curs = conn.cursor()
    x = curs.execute("SELECT COUNT(*) FROM INCIDENTS;").fetchall()
    assert x[0][0] == 495 

def test_digest(filename = 'docs/feb27_incidents.pdf'):
    tester = incidents.extractpdflocal(filename)
    parsed = incidents.parsepdf(tester)
    incidents.database(parsed)
    x = incidents.digest()
    total = 0
    for y in x:
        total += int(y[1])
    assert total == 495
