-- SQL SETUP

CREATE TABLE errorRequests(requestId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, requestText TEXT NOT NULL)  

-- TEST INSERTS

INSERT INTO errorRequests(requestText)
VALUES ("Test input 1"), ("Test Input 2")

SELECT * FROM errorRequests