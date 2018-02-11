CREATE DATABASE JDdb;

USE JDdb;

Drop table CURRENT;
Drop table HISTORY;

CREATE TABLE CURRENT(
CurrentId int(20) NOT NULL auto_increment,
CurItemId int(20) NOT NULL UNIQUE,
ItemName varchar(20) NOT NULL,
URL varchar(128) NOT NULL UNIQUE,
CurPrice double(10,2) NOT NULL,
UpdTimeVersion timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY  (CurrentId)
);

CREATE TABLE HISTORY(
HistoryId  int(20) NOT NULL auto_increment,
HisItemId int(20) NOT NULL UNIQUE,
HisPrice double(10,2) NOT NULL ,
GetTimeVersion timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY  (HistoryId)
);