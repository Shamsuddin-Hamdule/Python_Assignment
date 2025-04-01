----------------Question 1

mysql> create Database Assignment4;
Query OK, 1 row affected (0.16 sec)

mysql> use Assignment4
Database changed

mysql>  create table emp(
    ->     EmpID INT Primary Key,
    ->     Name VARCHAR(50) Not Null,
    ->     Age INT,
    ->     Department VARCHAR(50),
    ->     Salary Decimal(10,2),
    ->     JoiningDate DATE,
    ->     City VARCHAR(50)
    ->      );
Query OK, 0 rows affected (0.15 sec)

----------------Question 2

mysql>
mysql> INSERT INTO emp VALUES(1, 'Rajesh Kumar', 28, 'IT', 55000.00, '2022-03-15', 'Bangalore');
Query OK, 1 row affected (0.03 sec)

mysql> INSERT INTO emp VALUES(2, 'Amit Sharma', 32, 'HR', 48000.00, '2021-06-20', 'Mumbai');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO emp VALUES(3, 'Suresh Patel', 35, 'Finance', 62000.00, '2020-11-10', 'Delhi');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO emp VALUES(4, 'Vikram Singh', 29, 'Marketing', 51000.00, '2022-01-05', 'Chennai');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO emp VALUES(5, 'Arun Verma', 31, 'IT', 58000.00, '2021-09-12', 'Hyderabad');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO emp VALUES(6, 'Deepak Gupta', 27, 'Operations', 45000.00, '2022-07-25', 'Pune');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO emp VALUES(7, 'Rahul Mishra', 33, 'Finance', 59000.00, '2021-04-18', 'Kolkata');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO emp VALUES(8, 'Mohan Krishna', 30, 'HR', 47000.00, '2022-02-28', 'Mumbai');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO emp VALUES(9, 'Sanjay Yadav', 34, 'Marketing', 53000.00, '2021-08-15', 'Delhi');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO emp VALUES(10, 'Karthik Reddy', 29, 'IT', 56000.00, '2022-05-01', 'Bangalore');
Query OK, 1 row affected (0.01 sec)

----------------Question 3

mysql> SELECT * FROM EMP;
+-------+---------------+------+------------+----------+-------------+-----------+
| EmpID | Name          | Age  | Department | Salary   | JoiningDate | City      |
+-------+---------------+------+------------+----------+-------------+-----------+
|     1 | Rajesh Kumar  |   28 | IT         | 55000.00 | 2022-03-15  | Bangalore |
|     2 | Amit Sharma   |   32 | HR         | 48000.00 | 2021-06-20  | Mumbai    |
|     3 | Suresh Patel  |   35 | Finance    | 62000.00 | 2020-11-10  | Delhi     |
|     4 | Vikram Singh  |   29 | Marketing  | 51000.00 | 2022-01-05  | Chennai   |
|     5 | Arun Verma    |   31 | IT         | 58000.00 | 2021-09-12  | Hyderabad |
|     6 | Deepak Gupta  |   27 | Operations | 45000.00 | 2022-07-25  | Pune      |
|     7 | Rahul Mishra  |   33 | Finance    | 59000.00 | 2021-04-18  | Kolkata   |
|     8 | Mohan Krishna |   30 | HR         | 47000.00 | 2022-02-28  | Mumbai    |
|     9 | Sanjay Yadav  |   34 | Marketing  | 53000.00 | 2021-08-15  | Delhi     |
|    10 | Karthik Reddy |   29 | IT         | 56000.00 | 2022-05-01  | Bangalore |
+-------+---------------+------+------------+----------+-------------+-----------+
10 rows in set (0.02 sec)

mysql> SELECT Name, Department, Salary FROM EMP;
+---------------+------------+----------+
| Name          | Department | Salary   |
+---------------+------------+----------+
| Rajesh Kumar  | IT         | 55000.00 |
| Amit Sharma   | HR         | 48000.00 |
| Suresh Patel  | Finance    | 62000.00 |
| Vikram Singh  | Marketing  | 51000.00 |
| Arun Verma    | IT         | 58000.00 |
| Deepak Gupta  | Operations | 45000.00 |
| Rahul Mishra  | Finance    | 59000.00 |
| Mohan Krishna | HR         | 47000.00 |
| Sanjay Yadav  | Marketing  | 53000.00 |
| Karthik Reddy | IT         | 56000.00 |
+---------------+------------+----------+
10 rows in set (0.01 sec)

----------------Question 5

mysql> Select * from EMP where salary > 50000;
+-------+---------------+------+------------+----------+-------------+-----------+
| EmpID | Name          | Age  | Department | Salary   | JoiningDate | City      |
+-------+---------------+------+------------+----------+-------------+-----------+
|     1 | Rajesh Kumar  |   28 | IT         | 55000.00 | 2022-03-15  | Bangalore |
|     3 | Suresh Patel  |   35 | Finance    | 62000.00 | 2020-11-10  | Delhi     |
|     4 | Vikram Singh  |   29 | Marketing  | 51000.00 | 2022-01-05  | Chennai   |
|     5 | Arun Verma    |   31 | IT         | 58000.00 | 2021-09-12  | Hyderabad |
|     7 | Rahul Mishra  |   33 | Finance    | 59000.00 | 2021-04-18  | Kolkata   |
|     9 | Sanjay Yadav  |   34 | Marketing  | 53000.00 | 2021-08-15  | Delhi     |
|    10 | Karthik Reddy |   29 | IT         | 56000.00 | 2022-05-01  | Bangalore |
+-------+---------------+------+------------+----------+-------------+-----------+
7 rows in set (0.02 sec)

----------------Question 6

mysql> Select * from EMP where Department = 'IT';
+-------+---------------+------+------------+----------+-------------+-----------+
| EmpID | Name          | Age  | Department | Salary   | JoiningDate | City      |
+-------+---------------+------+------------+----------+-------------+-----------+
|     1 | Rajesh Kumar  |   28 | IT         | 55000.00 | 2022-03-15  | Bangalore |
|     5 | Arun Verma    |   31 | IT         | 58000.00 | 2021-09-12  | Hyderabad |
|    10 | Karthik Reddy |   29 | IT         | 56000.00 | 2022-05-01  | Bangalore |
+-------+---------------+------+------------+----------+-------------+-----------+
3 rows in set (0.01 sec)

----------------Question 7

mysql> SELECT * FROM EMP WHERE Age BETWEEN 25 AND 35;
+-------+---------------+------+------------+----------+-------------+-----------+
| EmpID | Name          | Age  | Department | Salary   | JoiningDate | City      |
+-------+---------------+------+------------+----------+-------------+-----------+
|     1 | Rajesh Kumar  |   28 | IT         | 55000.00 | 2022-03-15  | Bangalore |
|     2 | Amit Sharma   |   32 | HR         | 48000.00 | 2021-06-20  | Mumbai    |
|     3 | Suresh Patel  |   35 | Finance    | 62000.00 | 2020-11-10  | Delhi     |
|     4 | Vikram Singh  |   29 | Marketing  | 51000.00 | 2022-01-05  | Chennai   |
|     5 | Arun Verma    |   31 | IT         | 58000.00 | 2021-09-12  | Hyderabad |
|     6 | Deepak Gupta  |   27 | Operations | 45000.00 | 2022-07-25  | Pune      |
|     7 | Rahul Mishra  |   33 | Finance    | 59000.00 | 2021-04-18  | Kolkata   |
|     8 | Mohan Krishna |   30 | HR         | 47000.00 | 2022-02-28  | Mumbai    |
|     9 | Sanjay Yadav  |   34 | Marketing  | 53000.00 | 2021-08-15  | Delhi     |
|    10 | Karthik Reddy |   29 | IT         | 56000.00 | 2022-05-01  | Bangalore |
+-------+---------------+------+------------+----------+-------------+-----------+
10 rows in set (0.01 sec)

----------------Question 8

mysql> SELECT * FROM EMP WHERE JoiningDate > '2022-01-01';
+-------+---------------+------+------------+----------+-------------+-----------+
| EmpID | Name          | Age  | Department | Salary   | JoiningDate | City      |
+-------+---------------+------+------------+----------+-------------+-----------+
|     1 | Rajesh Kumar  |   28 | IT         | 55000.00 | 2022-03-15  | Bangalore |
|     4 | Vikram Singh  |   29 | Marketing  | 51000.00 | 2022-01-05  | Chennai   |
|     6 | Deepak Gupta  |   27 | Operations | 45000.00 | 2022-07-25  | Pune      |
|     8 | Mohan Krishna |   30 | HR         | 47000.00 | 2022-02-28  | Mumbai    |
|    10 | Karthik Reddy |   29 | IT         | 56000.00 | 2022-05-01  | Bangalore |
+-------+---------------+------+------------+----------+-------------+-----------+
5 rows in set (0.01 sec)

----------------Question 9

mysql> SELECT * FROM EMP WHERE City IN ('Mumbai', 'Pune');
+-------+---------------+------+------------+----------+-------------+--------+
| EmpID | Name          | Age  | Department | Salary   | JoiningDate | City   |
+-------+---------------+------+------------+----------+-------------+--------+
|     2 | Amit Sharma   |   32 | HR         | 48000.00 | 2021-06-20  | Mumbai |
|     6 | Deepak Gupta  |   27 | Operations | 45000.00 | 2022-07-25  | Pune   |
|     8 | Mohan Krishna |   30 | HR         | 47000.00 | 2022-02-28  | Mumbai |
+-------+---------------+------+------------+----------+-------------+--------+
3 rows in set (0.01 sec)

----------------Question 10

mysql> SELECT Department, COUNT(*) as EmpCount FROM EMP GROUP BY Department;
+------------+----------+
| Department | EmpCount |
+------------+----------+
| IT         |        3 |
| HR         |        2 |
| Finance    |        2 |
| Marketing  |        2 |
| Operations |        1 |
+------------+----------+
5 rows in set (0.02 sec)

----------------Question 11

mysql> SELECT Department, AVG(Salary) as AvgSalary FROM EMP GROUP BY Department;
+------------+--------------+
| Department | AvgSalary    |
+------------+--------------+
| IT         | 56333.333333 |
| HR         | 47500.000000 |
| Finance    | 60500.000000 |
| Marketing  | 52000.000000 |
| Operations | 45000.000000 |
+------------+--------------+
5 rows in set (0.01 sec)

----------------Question 12

mysql> SELECT * FROM EMP WHERE Salary = (SELECT MAX(Salary) FROM EMP);
+-------+--------------+------+------------+----------+-------------+-------+
| EmpID | Name         | Age  | Department | Salary   | JoiningDate | City  |
+-------+--------------+------+------------+----------+-------------+-------+
|     3 | Suresh Patel |   35 | Finance    | 62000.00 | 2020-11-10  | Delhi |
+-------+--------------+------+------------+----------+-------------+-------+
1 row in set (0.05 sec)

----------------Question 13

mysql> SELECT * FROM EMP ORDER BY Salary DESC LIMIT 3;
+-------+--------------+------+------------+----------+-------------+-----------+
| EmpID | Name         | Age  | Department | Salary   | JoiningDate | City      |
+-------+--------------+------+------------+----------+-------------+-----------+
|     3 | Suresh Patel |   35 | Finance    | 62000.00 | 2020-11-10  | Delhi     |
|     7 | Rahul Mishra |   33 | Finance    | 59000.00 | 2021-04-18  | Kolkata   |
|     5 | Arun Verma   |   31 | IT         | 58000.00 | 2021-09-12  | Hyderabad |
+-------+--------------+------+------------+----------+-------------+-----------+
3 rows in set (0.01 sec)

----------------Question 14

mysql> SELECT * FROM EMP ORDER BY Name ASC, Salary DESC;
+-------+---------------+------+------------+----------+-------------+-----------+
| EmpID | Name          | Age  | Department | Salary   | JoiningDate | City      |
+-------+---------------+------+------------+----------+-------------+-----------+
|     2 | Amit Sharma   |   32 | HR         | 48000.00 | 2021-06-20  | Mumbai    |
|     5 | Arun Verma    |   31 | IT         | 58000.00 | 2021-09-12  | Hyderabad |
|     6 | Deepak Gupta  |   27 | Operations | 45000.00 | 2022-07-25  | Pune      |
|    10 | Karthik Reddy |   29 | IT         | 56000.00 | 2022-05-01  | Bangalore |
|     8 | Mohan Krishna |   30 | HR         | 47000.00 | 2022-02-28  | Mumbai    |
|     7 | Rahul Mishra  |   33 | Finance    | 59000.00 | 2021-04-18  | Kolkata   |
|     1 | Rajesh Kumar  |   28 | IT         | 55000.00 | 2022-03-15  | Bangalore |
|     9 | Sanjay Yadav  |   34 | Marketing  | 53000.00 | 2021-08-15  | Delhi     |
|     3 | Suresh Patel  |   35 | Finance    | 62000.00 | 2020-11-10  | Delhi     |
|     4 | Vikram Singh  |   29 | Marketing  | 51000.00 | 2022-01-05  | Chennai   |
+-------+---------------+------+------------+----------+-------------+-----------+
10 rows in set (0.00 sec)

----------------Question 15

mysql> UPDATE EMP SET Salary = Salary * 1.1 WHERE Department = 'IT';
Query OK, 3 rows affected (0.03 sec)
Rows matched: 3  Changed: 3  Warnings: 0

----------------Question 16

mysql> DELETE FROM EMP WHERE Department = 'HR';
Query OK, 2 rows affected (0.02 sec)

----------------Question 17

mysql> create table projects(
    ->
    -> ProjectID INT Primary Key,
    ->
    -> ProjectName VARCHAR(50),
    ->
    -> EmpID INT,
    ->
    -> StartDate DATE,
    ->
    -> EndDate DATE,
    ->
    -> FOREIGN KEY(EmpID) REFERENCES EMP (EmpID)
    -> );
Query OK, 0 rows affected (0.13 sec)

----------------Question 18

----------------Question 19

----------------Question 20