# Implementing-server-using-flask

About the project: Implement server using “flask” microframework and test it useing "pytest" framework.
There are two files - app.py which implements the server and test.py that tests the server.

The server includes the following API's: POST/AddMessage , Get/GetMessage, Get/DeleteMessage :

The data is stored as JSON
AddMessage - Creates a new message in the server. 
GetMessage - Returns data according to the url query.
DeleteMessage - Deletes data according to the url query.

Project's installations that are needed:

Install python

Choose an environment to work in, for example visual studio code

Install pip

Install virtualenv, open a file and activate it

Install flask

Install requests

Install pytest

Runing the project:
1. Run the server (python app.py)
2. With a different cmd - run the test (pytest test.py)

The test plan for the API’s I implemented:
1. Testing that adding, deleting and getting messages is done succesfully
2. Testing edge cases such as wrong values, wrong keys, size of messages, etc

Plans for the future:
1. Adding more tests of edge cases that would be done generically
2. Testing the messages that are stored after operations are done
3. Using a database to store the data
