from utils import *

sql = """
USE PYTHON;
DROP TABLE IF EXISTS PYTHON.SALARY_TABLE;
CREATE TABLE PYTHON.SALARY_TABLE
  (NAME   VARCHAR(20) PRIMARY KEY,
   SALARY FLOAT);

insert into SALARY_TABLE values ('James',   27300.00);
insert into SALARY_TABLE values ('Mary',    35800.00);
insert into SALARY_TABLE values ('Beth',    25500.00);
insert into SALARY_TABLE values ('Charles', 41000.00);
insert into SALARY_TABLE values ('Maud',    34100.00);
insert into SALARY_TABLE values ('Henry',   36600.00);
insert into SALARY_TABLE values ('Richard', 21000.00);
insert into SALARY_TABLE values ('Edward',  16900.00);

COMMIT;
"""

connection = getConnection()
cursor = connection.cursor(buffered=True)
cursor.execute(sql)
connection.close()
