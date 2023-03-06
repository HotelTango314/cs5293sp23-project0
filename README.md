# PROJECT 0 README
## HENRY THOMAS [[[]]]  CS5293 SP23

### 1. HOW TO INSTALL

pipenv install project0

### 2. HOW TO RUN

to pull live data from Norman PD: 

pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-27\_daily\_incident\_summary.pdf

to utilize the example document saved locally:

pipenv run python project0/main.py --incidents docs/feb27\_incidents.pdf --local

### 3. VIDEO DEMONSTRATING HOW TO RUN AVAILABLE AT YOUTUBE LINK BELOW:
[title](https://youtu.be/emlq09IEox0)

### 4. DESCRIBE ALL FUNCTIONS:
**A. getpdf(url)**
This function downloads a PDF file from the world wide web through a user provided URL.
It takes a url to a pdf file on the web
It returns a string object which is the data inside the PDF
GOTCHA: this method is only invoked when using a file direct from the web
Alternatively, you can use a file saved locally (using --local tag in run command)

**B. extractpdflocal(data)**
This function converts a .pdf file into a PdfReader object.
It takes a pdf file stored locally
It returns a PdfReader object
GOTCHA: this method is only involved when using a file saved locally

**C. extractpdf(data)**
This function converts a urllib string object into a PdfReader object
It takes a URLLIB object
It returns a PdfReader object
GOTCHA: this method is only inolved when using a pdf file direct from the web

**D. jt(list)**
The findall() method in Python's re package returns each match group in a separate index of a list.
Many of them are blank, this method combines all the list elements into one string and cuts the blank space off the end

**E. parsepdf(data)**
This function takes a PdfReader object and applies regular expressions to match datafields.
It then combies each record into a row of a table (a list of lists)
The completed "table" is then returned

**F. database (parsed data)**
This function receives the list of lists created by parsepdf(), creates a sqlite database and inserts the data to the database.

**G. digest()**
This function utilizes the database created by the database() method to query the full list of natures, count up the number of occurrences of each, and then returns the list of rows of data (the nature, and the number of occurrences) The output is then formatted and displayed directly from the main method. I did it this way so that when calling this method during testing the regular output is not displayed, only the results of the assertion

### 5. BUGS AND ASSUMPTIONS
Bugs - the REGEX pulling the address is 100% accurate for this file, and edge cases in the test file were fully accounted for. There may be other edge cases in other files that have not been considered and will not be fully identified by the regex.

### 6. DATABASE DEVELOPMENT
The data is converted from PDF to a "table" (a list of lists) and then is inserted to the sqlite database. The database is set to drop the existing table at the start of each run so results from the run will be only the results for the latest PDF file uploaded to the databse. Data from all previous pdf files are deleted when the new pdf file is uploaded.

### 7. TESTING
The there are 7 tests in total performed by the program when

```
pipenv run python -m pytest
```
command is entered. Except for getpdf() and 

test\_getpdf() looks for the %PDF-1.5 marker at the start of the file to confirm that a PDF file has been downloaded

test\_extractpdf() calls the .pdf\_header attribute to ensure it contains %PDF-1.5 marker at the start of the file

test\_extractpdflocal() calls the .pdf\_header attribute to ensure it contains %PDF-1.5 marker at the start of the file

test\_jt() takes the following list: [' ',' ','h','e','l','l','o',' ',' '] applies the method and then checks to see if the result is a string of the form 'hello'.

test\_parsepdf() knowing that there are 495 records in our locally saved test file, it checks to ensure that the "table" (list of lists) returned by parsepdf() is 495 records long and 5 fields wide.

test\_database() runs the database() method to create the database and then connects to the database (norman.db) and checks to ensure that there are 495 rows saved in the databse table.

test\_digest() runs the digest() method and then sums up the total of all the occurrences tabulated by the method, which should be equal to the number of records in the table, 495.
