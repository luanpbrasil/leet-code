/* Solution of the problem 182 - Duplicate Emails:
    https://leetcode.com/problems/duplicate-emails/
*/
SELECT p.email AS "Email"
FROM Person p
GROUP BY p.email
HAVING COUNT(id)>1;