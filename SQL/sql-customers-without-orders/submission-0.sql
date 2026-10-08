-- Write your query below
WITH distinct_customers AS (SELECT DISTINCT customer_id FROM orders)

SELECT name
FROM customers
LEFT JOIN distinct_customers ON distinct_customers.customer_id = customers.id
WHERE distinct_customers.customer_id IS NULL