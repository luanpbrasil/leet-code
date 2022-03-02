/* Solution of the problem 183 - Customers Who Never Order:
    https://leetcode.com/problems/customers-who-never-order/
*/

/*First solution - using LEFT JOIN clause*/
SELECT c.name AS "Customers"
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;

/*First solution - using NOT IN clause*/
SELECT customers.name AS 'Customers'
FROM customers
WHERE customers.id NOT IN
(
    SELECT customerid FROM orders
);