## Wyatt Turbeville Capstone Project
# Research Database and Front End CRUD Application
## Milestone 3 Video
https://vimeo.com/1078774640/ad9073c792?share=copy

## Description
The goal of this project can be summed up to two points
1. Create a Database in which Dr. Fuenzalida Valenzuela can store the entries of bacteria culture data related to her research
2. Provide a front end CRUD web application to easily create, delete, modify, and query collected data for presentation

## Progress
### Hello.py
This is the default routing page for a Flask web application. This page handles requesting data from the MySql Server, HTML routing requests, function logic, and displaying
webpages. By default it presents the index.html page to the user. It also handles the routing and logic behind 3 major actions. Load-content which sends html snippits to the JS
in index.html. Load-action which handles clicking one of the action buttons on a table. This will load the appropiate modal in response. Commit-data will handle taking in data
from a modal form and committing it to the database.

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
So far, there is a basic front end website and a complete database that can be populated at any time. The next steps are to create working action buttons that can
create, search, update, and delete entries in a selected table. This is argueably the most monumental task. After it is done however, then steps can be taken to stylize the
application page for aestetics as well as assess the need for any missing functions within the application. Possible additions would include generating an overview in 
the dashboard page as well as adding an export to csv option for selected data.
