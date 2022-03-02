/* Solution of the problem 196 - Delete Duplicate Emails:
    https://leetcode.com/problems/delete-duplicate-emails/
*/
DELETE p1 FROM Person p1
INNER JOIN Person p2
WHERE 
    p1.id > p2.id AND 
    p1.email = p2.email;