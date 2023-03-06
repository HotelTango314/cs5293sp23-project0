HENRY THOMAS
PROJECT 0 README

1. HOW TO INSTALL

pipenv install project0

1. HOW TO RUN

to pull live data from Norman PD: 

pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-27\_daily\_incident\_summary.pdf

to utilize the example document saved locally:

pipenv run python project0/main.py --incidents docs/feb27\_incidents.pdf --local

2. VIDEO DEMONSTRATING HOW TO RUN
https://youtu.be/emlq09IEox0

3. DESCRIBE ALL FUNCTIONS:
A. getpdf(url)
This function downloads a PDF file from the world wide web through a user provided URL.
It takes a url to a pdf file on the web
It returns a string object which is the data inside the PDF
GOTCHA: this method is only invoked when using a file direct from the web
Alternatively, you can use a file saved locally (using --local tag in run command)

B. extractpdflocal(data)
This function converts a .pdf file into a PdfReader object.
It takes a pdf file stored locally
It returns a PdfReader object
GOTCHA: this method is only involved when using a file saved locally

C. extractpdf(data)
This function converts a urllib string object into a PdfReader object
It takes a URLLIB object
It returns a PdfReader object
GOTCHA: this method is only inolved when using a pdf file direct from the web

D. jt
The findall() method in Python's re package returns each match group in a separate index of a list.
Many of them are blank, this method combines all the list elements into one string and cuts the blank space off the end

E. parsepdf(data)
This function takes a PdfReader object and applies regular expressions to match datafields.
It then combies each record into a row of a table (a list of lists)
The completed "table" is then returned

F. database(parsed\_data)
This function receives the list of lists created by parsepdf(), creates a sqlite database and inserts the data to the database.

G. digest()
This function utilizes the database created by the database() method to query the full list of natures, count up the number of occurrences of each, and then returns the list of rows of data (the nature, and the number of occurrences) The output is then formatted and displayed directly from the main method. I did it this way so that when calling this method during testing the regular output is not displayed, only the results of the assertion

4. BUGS AND ASSUMPTIONS
Bugs - the REGEX pulling the address is 100% accurate for this file, and edge cases in the test file were fully accounted for. There may be other edge cases in other files that have not been considered and will not be fully identified by the regex.

5. DATABASE DEVELOPMENT
The data is converted from PDF to a "table" (a list of lists) and then is inserted to the sqlite database. The database is set to drop the existing table at the start of each run so results from the run will be only the results for the latest PDF file uploaded to the databse. Data from all previous pdf files are deleted when the new pdf file is uploaded.
		
