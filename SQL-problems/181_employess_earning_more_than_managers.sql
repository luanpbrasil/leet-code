/* Solution of the problem 181 - Employees Earning More Than Their Managers: 
    https://leetcode.com/problems/employees-earning-more-than-their-managers/
*/
SELECT a.name AS "Employee" 
FROM Employee a, Employee b
WHERE a.managerId = b.Id
AND a.salary > b.salary;