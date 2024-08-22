1. Calculate the total revenue generated from sales for each product category.
Query:

SELECT p.category, SUM(s.total_price) AS total_revenue
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
GROUP BY p.category;
Output:

category	total_revenue
Electronics	3630.00
Explanation:

This query joins the Sales and Products tables on the product_id column, groups the results by product category, and calculates the total revenue for each category by summing up the total_price.

2. Find the product category with the highest average unit price.
Query:

SELECT category
FROM Products
GROUP BY category
ORDER BY AVG(unit_price) DESC
LIMIT 1;
Output:

category
Electronics
Explanation:

This query groups products by category, calculates the average unit price for each category, orders the results by the average unit price in descending order, and selects the top category with the highest average unit price using the LIMIT clause.

3. Identify products with total sales exceeding 30.
Query:

SELECT p.product_name
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
GROUP BY p.product_name
HAVING SUM(s.total_price) > 30;
Output:

product_name
Headphones
Keyboard
Laptop
Mouse
Smartphone
Explanation:

This query joins the Sales and Products tables on the product_id column, groups the results by product name, calculates the total sales revenue for each product, and selects products with total sales exceeding 30 using the HAVING clause.

4. Count the number of sales made in each month.
Query:

SELECT DATE_FORMAT(s.sale_date, '%Y-%m') AS month, COUNT(*) AS sales_count
FROM Sales s
GROUP BY month;
Output:

month

sales_count

2024-01

5

Explanation:

This query formats the sale_date column to extract the month and year, groups the results by month, and counts the number of sales made in each month.

5. Determine the average quantity sold for products with a unit price greater than $100.
Query:

SELECT AVG(s.quantity_sold) AS average_quantity_sold
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
WHERE p.unit_price > 100;
Output:

average_quantity_sold
4.0000
Explanation:

This query joins the Sales and Products tables on the product_id column, filters products with a unit price greater than $100, and calculates the average quantity sold for those products.

6. Retrieve the product name and total sales revenue for each product.
Query:

SELECT p.product_name, SUM(s.total_price) AS total_revenue
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
GROUP BY p.product_name;
Output:

product_name	total_revenue
Laptop	2500.00
Smartphone	900.00
Headphones	60.00
Keyboard	80.00
Mouse	90.00
Explanation:

This query joins the Sales and Products tables on the product_id column, groups the results by product name, and calculates the total sales revenue for each product.

7. List all sales along with the corresponding product names.
Query:

SELECT s.sale_id, p.product_name
FROM Sales s
JOIN Products p ON s.product_id = p.product_id;
Output:

sale_id	product_name
1	Laptop
2	Smartphone
3	Headphones
4	Keyboard
5	Mouse
Explanation:

This query joins the Sales and Products tables on the product_id column and retrieves the sale_id and product_name for each sale.

8. Retrieve the product name and total sales revenue for each product.
Query:

SELECT p.category, 
       SUM(s.total_price) AS category_revenue,
       (SUM(s.total_price) / (SELECT SUM(total_price) FROM Sales)) * 100 AS revenue_percentage
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue_percentage DESC
LIMIT 3;
Output:

category	category_revenue	revenue_percentage
Electronics	3630.00	100.000000
Explanation:

This query will give you the top three product categories contributing to the highest percentage of total revenue generated from sales. However, if you only have one category (Electronics) as in the provided sample data, it will be the only result.

9. Rank products based on total sales revenue.
Query:

SELECT p.product_name, SUM(s.total_price) AS total_revenue,
       RANK() OVER (ORDER BY SUM(s.total_price) DESC) AS revenue_rank
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
GROUP BY p.product_name;
Output:

product_name	total_revenue	revenue_rank
Laptop	2500.00	1
Smartphone	900.00	2
Mouse	90.00	3
Keyboard	80.00	4
Headphones	60.00	5
Explanation:

This query joins the Sales and Products tables on the product_id column, groups the results by product name, calculates the total sales revenue for each product, and ranks products based on total sales revenue using the RANK() window function.

10. Calculate the running total revenue for each product category.
Query:

SELECT p.category, p.product_name, s.sale_date, 
       SUM(s.total_price) OVER (PARTITION BY p.category ORDER BY s.sale_date) AS running_total_revenue
FROM Sales s
JOIN Products p ON s.product_id = p.product_id;
Output:

category	product_name	sale_date	running_total_revenue
Electronics	Laptop	2024-01-01	2500.00
Electronics	Smartphone	2024-01-02	3460.00
Electronics	Headphones	2024-01-02	3460.00
Electronics	Keyboard	2024-01-03	3630.00
Electronics	Mouse	2024-01-03	3630.00
Explanation:

This query joins the Sales and Products tables on the product_id column, partitions the results by product category, orders the results by sale date, and calculates the running total revenue for each product category using the SUM() window function.

11. Categorize sales as “High”, “Medium”, or “Low” based on total price (e.g., > $200 is High, $100-$200 is Medium, < $100 is Low).
Query:

SELECT sale_id, 
       CASE 
           WHEN total_price > 200 THEN 'High'
           WHEN total_price BETWEEN 100 AND 200 THEN 'Medium'
           ELSE 'Low'
       END AS sales_category
FROM Sales;
Output:

sale_id	sales_category
1	High
2	High
3	Low
4	Low
5	Low
Explanation:

This query categorizes sales based on total price using a CASE statement. Sales with a total price greater than $200 are categorized as “High”, sales with a total price between $100 and $200 are categorized as “Medium”, and sales with a total price less than $100 are categorized as “Low”.

12. Identify sales where the quantity sold is greater than the average quantity sold.
Query:

SELECT *
FROM Sales
WHERE quantity_sold > (SELECT AVG(quantity_sold) FROM Sales);
Output:

sale_id	product_id	quantity_sold	sale_date	total_price
1	101	5	2024-01-01	2500.00
5	105	6	2024-01-03	90.00
Explanation:

This query selects all sales where the quantity sold is greater than the average quantity sold across all sales in the Sales table.

13. Extract the month and year from the sale date and count the number of sales for each month.
Query:

SELECT CONCAT(YEAR(sale_date), '-', LPAD(MONTH(sale_date), 2, '0')) AS month,
       COUNT(*) AS sales_count
FROM Sales
GROUP BY YEAR(sale_date), MONTH(sale_date);
Output:

month

sales_count

2024-01

5

Explanation:

This query selects all sales where the quantity sold is greater than the average quantity sold across all sales in the Sales table.

14. Calculate the number of days between the current date and the sale date for each sale.
Query:

SELECT sale_id, DATEDIFF(NOW(), sale_date) AS days_since_sale
FROM Sales;
Output:

sale_id

days_since_sale

1

185

2

184

3

184

4

183

5

183

Explanation:

This query calculates the number of days between the current date and the sale date for each sale using the DATEDIFF function.

15. Identify sales made during weekdays versus weekends.
Query:

SELECT sale_id,
       CASE 
           WHEN DAYOFWEEK(sale_date) IN (1, 7) THEN 'Weekend'
           ELSE 'Weekday'
       END AS day_type
FROM Sales;
Output:

sale_id

day_type

1

Weekday

2

Weekday

3

Weekday

4

Weekend

5

Weekend

Explanation:

This query categorizes sales based on the day of the week using the DAYOFWEEK function. Sales made on Sunday (1) or Saturday (7) are categorized as “Weekend”, while sales made on other days are categorized as “Weekday”.

