'''
1. Login with:
    sudo mysql -u root -p

2. Check security policy for passwords
    SHOW VARIABLES LIKE 'validate_password%';

3. Change security policy for passwords:
    SET GLOBAL validate_password.policy=LOW;

4. Create theUser with password=thePassword:
    CREATE USER 'theUser'@'localhost' IDENTIFIED BY 'thePassword';

5. Grant privileges:
    GRANT ALL PRIVILEGES ON *.* TO 'theUser'@'localhost' WITH GRANT OPTION;

6. Show all users:
    SELECT user FROM mysql.user;

'''


