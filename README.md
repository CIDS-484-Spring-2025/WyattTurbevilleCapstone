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

## Templates
This folder serves as the storage for all of html pages and snippits availble to Flask and Jinja. Each of these serve their own unqiue function with their
purpose being expanded on below.
### Index.html
This serves as the main front page of the application and will host the navigation of tables as well as the tables themselves and and action buttons to preform operations on
the tables.
### Farm.html
This is called a snippit, which is used by Jinja template language. This piece in particular can be used to dynamically load the farm table into an html table
so that it can be displayed on the webpage. Eventually this page could be adapted to display any table data it is handed, and not just a specific one. This would make
table creation handling more dynamic and allow for less overall files within the code structure.
### Dashboard.html
This is currently a placeholder. Purpose could be assigned later, such as displaying the total amount of samples collected or the total amount of tests run within the database.
### Modal.html
I am currently fighting this piece in an uphill battle. Its purpose is to dynamically create a form inside of a modal that allows the user to create a row entry into a table.
However, it is proving hard to accomplish as data types within a form are not uniform like they are within the table data object inside Farm.html
I will either complete this or move to an iterative solution instead.

## Moving Forward
Now that I have a solid understanding of the back and forth between the web sever and the database server there is much to do.
The first step will be to create an ER Diagram and fully create the database in a format that will hold all of the data values.
The next step will then be to create a usable front end that allows for creation, deletion, and viewing of records
After that, will the the step of writing the queries and functions required to have the web server and database communicate
Once these are completed, refining the overall design and deploying the application for use will be visited.
