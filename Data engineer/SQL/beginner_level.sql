---Beginner level concepts:
---Basic Retrieval
--Filtering
--Arithmetic Operations and Comparisons:
--Formatting
--Aggregation Functions

Create Sales table
-- Create Sales table

CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE,
    total_price DECIMAL(10, 2)
);

-- Insert sample data into Sales table

INSERT INTO Sales (sale_id, product_id, quantity_sold, sale_date, total_price) VALUES
(1, 101, 5, '2024-01-01', 2500.00),
(2, 102, 3, '2024-01-02', 900.00),
(3, 103, 2, '2024-01-02', 60.00),
(4, 104, 4, '2024-01-03', 80.00),
(5, 105, 6, '2024-01-03', 90.00);
Output:

sale_id	product_id	quantity_sold	sale_date	total_price
1	101	5	2024-01-01	2500.00
2	102	3	2024-01-02	900.00
3	103	2	2024-01-02	60.00
4	104	4	2024-01-03	80.00
5	105	6	2024-01-03	90.00
Create Products table
-- Create Products table

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10, 2)
);

-- Insert sample data into Products table

INSERT INTO Products (product_id, product_name, category, unit_price) VALUES
(101, 'Laptop', 'Electronics', 500.00),
(102, 'Smartphone', 'Electronics', 300.00),
(103, 'Headphones', 'Electronics', 30.00),
(104, 'Keyboard', 'Electronics', 20.00),
(105, 'Mouse', 'Electronics', 15.00);
Output:

product_id	product_name	category	unit_price
101	Laptop	Electronics	500.00
102	Smartphone	Electronics	300.00
103	Headphones	Electronics	30.00
104	Keyboard	Electronics	20.00
105	Mouse	Electronics	15.00
SQL Practice Exercises for Beginners
This hands-on approach provides a practical environment for beginners to experiment with various SQL commands, gaining confidence through real-world scenarios. By working through these exercises, newcomers can solidify their understanding of fundamental concepts like data retrieval, filtering, and manipulation, laying a strong foundation for their SQL journey.

1. Retrieve all columns from the Sales table.
Query:

SELECT * FROM Sales;
Output:

sale_id	product_id	quantity_sold	sale_date	total_price
1	101	5	2024-01-01	2500.00
2	102	3	2024-01-02	900.00
3	103	2	2024-01-02	60.00
4	104	4	2024-01-03	80.00
5	105	6	2024-01-03	90.00
Explanation:

This SQL query selects all columns from the Sales table, denoted by the asterisk (*) wildcard. It retrieves every row and all associated columns from the Sales table.

2. Retrieve the product_name and unit_price from the Products table.
Query:

SELECT product_name, unit_price FROM Products;
Output:

product_name	unit_price
Laptop	500.00
Smartphone	300.00
Headphones	30.00
Keyboard	20.00
Mouse	15.00
Explanation:

This SQL query selects the product_name and unit_price columns from the Products table. It retrieves every row but only the specified columns, which are product_name and unit_price.

3. Retrieve the sale_id and sale_date from the Sales table.
Query:

SELECT sale_id, sale_date FROM Sales;
Output:

sale_id	sale_date
1	2024-01-01
2	2024-01-02
3	2024-01-02
4	2024-01-03
5	2024-01-03
Explanation:

This SQL query selects the sale_id and sale_date columns from the Sales table. It retrieves every row but only the specified columns, which are sale_id and sale_date.

4. Filter the Sales table to show only sales with a total_price greater than $100.
Query:

SELECT * FROM Sales WHERE total_price > 100;
Output:

sale_id	product_id	quantity_sold	sale_date	total_price
1	101	5	2024-01-01	2500.00
2	102	3	2024-01-02	900.00
Explanation:

This SQL query selects all columns from the Sales table but only returns rows where the total_price column is greater than 100. It filters out sales with a total_price less than or equal to $100.

5. Filter the Products table to show only products in the ‘Electronics’ category.
Query:

SELECT * FROM Products WHERE category = 'Electronics';
Output:

product_id	product_name	category	unit_price
101	Laptop	Electronics	500.00
102	Smartphone	Electronics	300.00
103	Headphones	Electronics	30.00
104	Keyboard	Electronics	20.00
105	Mouse	Electronics	15.00
Explanation:

This SQL query selects all columns from the Products table but only returns rows where the category column equals ‘Electronics’. It filters out products that do not belong to the ‘Electronics’ category.

6. Retrieve the sale_id and total_price from the Sales table for sales made on January 3, 2024.
Query:

SELECT sale_id, total_price 
FROM Sales 
WHERE sale_date = '2024-01-03';
Output:

sale_id	total_price
4	80.00
5	90.00
Explanation:

This SQL query selects the sale_id and total_price columns from the Sales table but only returns rows where the sale_date is equal to ‘2024-01-03’. It filters out sales made on any other date.

7. Retrieve the product_id and product_name from the Products table for products with a unit_price greater than $100.
Query:

SELECT product_id, product_name 
FROM Products 
WHERE unit_price > 100;
Output:

product_id	product_name
101	Laptop
102	Smartphone
Explanation:

This SQL query selects the product_id and product_name columns from the Products table but only returns rows where the unit_price is greater than $100. It filters out products with a unit_price less than or equal to $100.

8. Calculate the total revenue generated from all sales in the Sales table.
Query:

SELECT SUM(total_price) AS total_revenue 
FROM Sales;
total_revenue
3630.00
Explanation:

This SQL query calculates the total revenue generated from all sales by summing up the total_price column in the Sales table using the SUM() function.

9. Calculate the average unit_price of products in the Products table.
Query:

SELECT AVG(unit_price) AS average_unit_price 
FROM Products;
Output:

average_unit_price
173
Explanation:

This SQL query calculates the average unit_price of products by averaging the values in the unit_price column in the Products table using the AVG() function.

10. Calculate the total quantity_sold from the Sales table.
Query:

SELECT SUM(quantity_sold) AS total_quantity_sold 
FROM Sales;
Output:

total_quantity_sold
20
Explanation:

This SQL query calculates the total quantity_sold by summing up the quantity_sold column in the Sales table using the SUM() function.

11. Retrieve the sale_id, product_id, and total_price from the Sales table for sales with a quantity_sold greater than 4.
Query:

SELECT sale_id, product_id, total_price 
FROM Sales 
WHERE quantity_sold > 4;
Output:

sale_id	product_id	total_price
1	101	2500.00
5	105	90.00
Explanation:

This SQL query selects the sale_id, product_id, and total_price columns from the Sales table but only returns rows where the quantity_sold is greater than 4.

12. Retrieve the product_name and unit_price from the Products table, ordering the results by unit_price in descending order.
Query:

SELECT product_name, unit_price 
FROM Products 
ORDER BY unit_price DESC;
Output:

product_name	unit_price
Laptop	500.00
Smartphone	300.00
Headphones	30.00
Keyboard	20.00
Mouse	15.00
Explanation:

This SQL query selects the product_name and unit_price columns from the Products table and orders the results by unit_price in descending order using the ORDER BY clause with the DESC keyword.

13. Retrieve the total_price of all sales, rounding the values to two decimal places.
Query:

SELECT ROUND(SUM(total_price), 2) AS total_sales 
FROM Sales;
Output:

product_name
3630.00
Explanation:

This SQL query calculates the total sales revenu by summing up the total_price column in the Sales table and rounds the result to two decimal places using the ROUND() function.

14. Calculate the average total_price of sales in the Sales table.
Query:

SELECT AVG(total_price) AS average_total_price 
FROM Sales;
Output:

average_total_price
726.000000
Explanation:

This SQL query calculates the average total_price of sales by averaging the values in the total_price column in the Sales table using the AVG() function.

15. Retrieve the sale_id and sale_date from the Sales table, formatting the sale_date as ‘YYYY-MM-DD’.
Query:

SELECT sale_id, DATE_FORMAT(sale_date, '%Y-%m-%d') AS formatted_date 
FROM Sales;
Output:

sale_id	formatted_date
1	2024-01-01
2	2024-01-02
3	2024-01-02
4	2024-01-03
5	2024-01-03
Explanation:

This SQL query selects the sale_id and sale_date columns from the Sales table and formats the sale_date using the DATE_FORMAT() function to display it in ‘YYYY-MM-DD’ format.

16. Calculate the total revenue generated from sales of products in the ‘Electronics’ category.
Query:

SELECT SUM(Sales.total_price) AS total_revenue 
FROM Sales 
JOIN Products ON Sales.product_id = Products.product_id 
WHERE Products.category = 'Electronics';
Output:

total_revenue
3630.00
Explanation:

This SQL query calculates the total revenue generated from sales of products in the ‘Electronics’ category by joining the Sales table with the Products table on the product_id column and filtering sales for products in the ‘Electronics’ category.

17. Retrieve the product_name and unit_price from the Products table, filtering the unit_price to show only values between $20 and $600.
Query:

SELECT product_name, unit_price 
FROM Products 
WHERE unit_price BETWEEN 20 AND 600;
Output:

product_name	unit_price
Laptop	500.00
Smartphone	300.00
Headphones	30.00
Keyboard	20.00
Explanation:

This SQL query selects the product_name and unit_price columns from the Products table but only returns rows where the unit_price falls within the range of $50 and $200 using the BETWEEN operator.

18. Retrieve the product_name and category from the Products table, ordering the results by category in ascending order.
Query:

SELECT product_name, category 
FROM Products 
ORDER BY category ASC;
Output:

product_name	category
Laptop	Electronics
Smartphone	Electronics
Headphones	Electronics
Keyboard	Electronics
Mouse	Electronics
Explanation:

This SQL query selects the product_name and category columns from the Products table and orders the results by category in ascending order using the ORDER BY clause with the ASC keyword.

19. Calculate the total quantity_sold of products in the ‘Electronics’ category.
Query:

SELECT SUM(quantity_sold) AS total_quantity_sold 
FROM Sales 
JOIN Products ON Sales.product_id = Products.product_id 
WHERE Products.category = 'Electronics';
Output:

total_quantity_sold
20
Explanation:

This SQL query calculates the total quantity_sold of products in the ‘Electronics’ category by joining the Sales table with the Products table on the product_id column and filtering sales for products in the ‘Electronics’ category.

20. Retrieve the product_name and total_price from the Sales table, calculating the total_price as quantity_sold multiplied by unit_price.
Query:

SELECT product_name, quantity_sold * unit_price AS total_price 
FROM Sales 
JOIN Products ON Sales.product_id = Products.product_id;
Output:

product_name	total_price
Laptop	2500.00
Smartphone	900.00
Headphones	60.00
Keyboard	80.00
Mouse	90.00
Explanation:

This SQL query retrieves the product_name from the Sales table and calculates the total_price by multiplying quantity_sold by unit_price, joining the Sales table with the Products table on the product_id column.
