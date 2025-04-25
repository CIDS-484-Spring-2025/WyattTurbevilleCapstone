## Wyatt Turbeville Capstone Project
# Research Database and Front End CRUD Application

## Description
The goal of this project can be summed up to two points
1. Create a Database in which Dr. Fuenzalida Valenzuela can store the entries of bacteria culture data related to her research
2. Provide a front end CRUD web application to easily create, delete, modify, and query collected data for presentation

## Progress
### Hello.py
This is the default routing page for a Flask web application. So far only a proof of concept has been set up to establish how exactly web servers connect to database servers.
There are two routes, home and paragrpah. Home is the default page, which will eventually become the query page. Right now the default index.html page is
set up to take in two inputs and on submit, pass them along to the paragraph route. The paragraph page then queries on the server side data from the database and passes it along
to the paragrpah.html page for display.

## Moving Forward
Now that I have a solid understanding of the back and forth between the web sever and the database server there is much to do.
The first step will be to create an ER Diagram and fully create the database in a format that will hold all of the data values.
The next step will then be to create a usable front end that allows for creation, deletion, and viewing of records
After that, will the the step of writing the queries and functions required to have the web server and database communicate
Once these are completed, refining the overall design and deploying the application for use will be visited.
