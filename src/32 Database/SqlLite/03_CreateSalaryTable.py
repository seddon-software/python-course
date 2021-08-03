from utils import *

sql = """
DROP TABLE IF EXISTS SALARY_TABLE;
CREATE TABLE SALARY_TABLE
  (NAME   text PRIMARY KEY,
   SALARY FLOAT);

insert into SALARY_TABLE values ('James',   27300.00);
insert into SALARY_TABLE values ('Mary',    35800.00);
insert into SALARY_TABLE values ('Beth',    25500.00);
insert into SALARY_TABLE values ('Charles', 41000.00);
insert into SALARY_TABLE values ('Maud',    34100.00);
insert into SALARY_TABLE values ('Henry',   36600.00);
insert into SALARY_TABLE values ('Richard', 21000.00);
insert into SALARY_TABLE values ('Edward',  16900.00);

"""

connection = getConnection("database.db")
cursor = connection.cursor()
cursor.executescript(sql)
connection.close()
