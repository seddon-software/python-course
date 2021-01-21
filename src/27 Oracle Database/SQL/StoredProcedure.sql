create or replace PROCEDURE PYTHON.Increase_Salary 
  (theName IN varchar2, 
   Increase IN float, 
   NewSalary IN OUT float)
  AS
  BEGIN
    UPDATE Salary_Table
    SET SALARY = SALARY + Increase
    WHERE NAME = theName;

    SELECT SALARY INTO NewSalary
    FROM Salary_Table
    WHERE NAME = theName;
  END;
