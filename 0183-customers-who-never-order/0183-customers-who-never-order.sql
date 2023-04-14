# Write your MySQL query statement below
 select name as customers from customers where not id in (select customerId from orders);