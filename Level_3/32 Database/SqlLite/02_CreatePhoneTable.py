from utils import *

sql = """
DROP TABLE IF EXISTS PHONE_TABLE;
CREATE TABLE PHONE_TABLE (
  FIRST_NAME text NOT NULL,
  LAST_NAME  text NOT NULL,
  PHONE_NUMBER text NOT NULL);

INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('James',		'Bond',          '746');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Chris',		'Seddon',        '159');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Peter',		'Smith',         '376');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Mary',		'Housegood',     '468');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Kay',		'Hayward',       '120');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Harry',		'Redknapp',      '593');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Chris',		'Jeffries',      '482');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Susan',		'Stevens',       '796');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Jerry',		'Black',         '152');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Sam',		'Stayman',       '864');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Roy',		'Young',         '758');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Viv',		'King',          '459');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Terry',		'Morris',        '759');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Kurt',		'Uhart',         '265');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Anne',		'Staniland',     '802');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Sue',		'Gerdes',        '806');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Ron',		'Cook',          '430');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Steve',		'Goodman',       '458');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Fred',		'Green',         '290');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Steven',		'Huftvin',       '482');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Kirk',		'Thompson',      '783');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Hugh',		'Jones',         '581');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Dave',		'Leeman',        '902');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Leroy',		'Gorman',        '945');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Dereck',		'Bell',          '268');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Paul',		'Younger',       '857');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Stuart',	'Ashen',         '923');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Jerry',		'Taylor',        '592');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Mike',		'Rumper',        '901');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Phillip',	'Haybrooke',     '700');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('Mary',		'MacMillan',     '450');
INSERT INTO PHONE_TABLE (FIRST_NAME, LAST_NAME, PHONE_NUMBER) values ('John',		'England',       '523');
"""

connection = getConnection("database.db")
cursor = connection.cursor()
cursor.executescript(sql)
connection.close()
