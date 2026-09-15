SELECT customer_id,
       COUNT(*) AS order_count,
       SUM(amount) AS total_amount
FROM orders
WHERE created_at >= '2026-09-01'
GROUP BY customer_id
ORDER BY total_amount DESC;
