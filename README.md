Editor: Davis Bosworth dboswor2@uoregon.edu

## Building/Running my Program in terminal
$ docker-compose build

$ docker-compose up

All APIs are on localhost port 5000. Individual API links on localhost:5001/APIname. The brevet calculator is on localhost:5003.

# Project 6: Brevet time calculator service
MongoDB database from project 5 and creates REST APIs for the user to choose from.

## What is in this repo

This program, with the help of flask and ajax, calculates ACP controle times. It is an attempt to duplicate the calculator found at https://rusa.org/octime_acp.html. A full list of the rules can be found at https://rusa.org/pages/acp-brevet-control-times-calculator. The km entered may not exceed the distance significantly. Open to close times on the first 0km will have 1 hour added. Km values cannot be negative. Values less than 20% of the original distance will be rounded down. Values less than the distance will be treated as normal.

This program uses the same logic with the addition of REST APIs. You can view all APIs on port 5000 or visit individual APIs through port 5001.

## Supported Links:
* "http://<host:port>/listAll" return all open and close times in the database
* "http://<host:port>/listOpenOnly" return open times only
* "http://<host:port>/listCloseOnly" return close times only

* "http://<host:port>/listAll/csv" return all open and close times in CSV format
* "http://<host:port>/listOpenOnly/csv" return open times only in CSV format
* "http://<host:port>/listCloseOnly/csv" return close times only in CSV format

* "http://<host:port>/listAll/json" return all open and close times in JSON format
* "http://<host:port>/listOpenOnly/json" return open times only in JSON format
* "http://<host:port>/listCloseOnly/json" return close times only in JSON format

* "http://<host:port>/listOpenOnly/csv?top=3" return top 3 open times only (in ascending order) in CSV format 
* "http://<host:port>/listOpenOnly/json?top=5" return top 5 open times only (in ascending order) in JSON format
* "http://<host:port>/listCloseOnly/csv?top=6" return top 5 close times only (in ascending order) in CSV format
* "http://<host:port>/listCloseOnly/json?top=4" return top 4 close times only (in ascending order) in JSON format
