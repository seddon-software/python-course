sql = """
DROP PROCEDURE IF EXISTS PYTHON.INCREASE_SALARY;
CREATE PROCEDURE PYTHON.INCREASE_SALARY(
    IN theName VARCHAR(20), 
    IN increase FLOAT, 
    OUT newSalary FLOAT)
BEGIN
    UPDATE SALARY_TABLE
    SET SALARY = SALARY + increase
    WHERE NAME = theName;

    SELECT SALARY INTO newSalary
    FROM SALARY_TABLE
    WHERE NAME = theName;
END;
"""
from utils import *

connection = getConnection()
cursor = connection.cursor(buffered=False)
cursor.execute(sql)

connection = getConnection()
cursor = connection.cursor(buffered=True)
args = ('Charles', 1000.0, 0.0) # 0.0 is to hold value of the OUT parameter
result = cursor.callproc('PYTHON.INCREASE_SALARY', args)
connection.commit()

print(f"Charles' new salary: {result[2]}")

