-- this is just a script to recreate the database that im
--  using in this website
CREATE DATABASE CalendarEvent2;
CREATE TABLE Event(
	title varchar(250),
    toDate DATETIME,
    fromDate DATETIME
);


USE CalendarEvent2;

-- for removing dynamic and direct query in the frontend 
-- securing the database
DELIMITER $$
CREATE PROCEDURE CalendarEvent2.addevent_proc3(IN TITLE VARCHAR(250),IN TODATE VARCHAR(250),IN FROMDATE VARCHAR(250))
BEGIN
	INSERT CalendarEvent2.Event(title,toDate,fromDate) VALUES(TITLE,
															 STR_TO_DATE(TODATE,'%Y-%m-%dT%H:%i:%s.%f'),
                                                             STR_TO_DATE(FROMDATE,'%Y-%m-%dT%H:%i:%s.%f'));
END
$$
DELIMITER;