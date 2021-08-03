USE PYTHON;

CREATE PROCEDURE PYTHON.Increase_Salary (
   IN theName varchar(20), 
   IN increase float, 
   OUT newSalary float)
  BEGIN
    UPDATE SALARY_TABLE
    SET SALARY = SALARY + increase
    WHERE NAME = theName;

    SELECT SALARY INTO newSalary
    FROM SALARY_TABLE
    WHERE NAME = theName;
  END;


