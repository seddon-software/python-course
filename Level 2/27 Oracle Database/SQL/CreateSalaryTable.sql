--************************************************************
--
--	Create Salary_Table
--
--************************************************************

  DROP TABLE Salary_Table;
  CREATE TABLE Salary_Table
    (NAME   VARCHAR2(20) PRIMARY KEY,
     SALARY FLOAT);


  insert into Salary_Table values ('James',   27300.00);
  insert into Salary_Table values ('Mary',    35800.00);
  insert into Salary_Table values ('Beth',    25500.00);
  insert into Salary_Table values ('Charles', 41000.00);
  insert into Salary_Table values ('Maud',    34100.00);
  insert into Salary_Table values ('Henry',   36600.00);
  insert into Salary_Table values ('Richard', 21000.00);
  insert into Salary_Table values ('Edward',  16900.00);

  SELECT * from Salary_Table;

