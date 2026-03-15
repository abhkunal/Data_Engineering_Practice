
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+

solution

Solution 1
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      #select ifnull ((select distinct salary from employee order by salary desc limit N, 1), null) as getNthHighestSalary
      (select Salary from Employee e1 where N-1=(select count(distinct(Salary)) from Employee e2 where e1.Salary < e2.salary) LIMIT 1)

  );
END

Solution 2

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      with cte as ( select salary, 
      dense_rank() over(order by salary desc)as rnk
      from employee)
      select max(distinct salary) as  getNthHighestSalary
      from cte 
      where rnk=n

  );
END