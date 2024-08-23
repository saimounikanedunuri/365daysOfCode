1. Write a query to create a view named Total_Sales that displays the total sales amount for each product along with their names and categories.
Query:

CREATE VIEW Total_Sales AS
SELECT p.product_name, p.category, SUM(s.total_price) AS total_sales_amount
FROM Products p
JOIN Sales s ON p.product_id = s.product_id
GROUP BY p.product_name, p.category;
SELECT * FROM Total_Sales;
Output:

product_name	category	total_sales_amount
Laptop	Electronics	2500.00
Smartphone	Electronics	900.00
Headphones	Electronics	60.00
Keyboard	Electronics	80.00
Mouse	Electronics	90.00
Explanation:

This query creates a view named Total_Sales that displays the total sales amount for each product along with their names and categories.

2. Retrieve the product details (name, category, unit price) for products that have a quantity sold greater than the average quantity sold across all products.
Query:

SELECT product_name, category, unit_price
FROM Products
WHERE product_id IN (
    SELECT product_id
    FROM Sales
    GROUP BY product_id
    HAVING SUM(quantity_sold) > (SELECT AVG(quantity_sold) FROM Sales)
);
Output:

product_name	category	unit_price
Laptop	Electronics	500.00
Mouse	Electronics	15.00
Explanation:

This query retrieves the product details (name, category, unit price) for products that have a quantity sold greater than the average quantity sold across all products.

3. Explain the significance of indexing in SQL databases and provide an example scenario where indexing could significantly improve query performance in the given schema.
Query:

-- Create an index on the sale_date column
CREATE INDEX idx_sale_date ON Sales (sale_date);

-- Query with indexing
SELECT *
FROM Sales
WHERE sale_date = '2024-01-03';
Output:

sale_id	product_id	quantity_sold	sale_date	total_price
4	104	4	2024-01-03	80.00
5	105	6	2024-01-03	90.00
Explanation:

With an index on the sale_date column, the database can quickly locate the rows that match the specified date without scanning the entire table. The index allows for efficient lookup of rows based on the sale_date value, resulting in improved query performance.

4. Add a foreign key constraint to the Sales table that references the product_id column in the Products table.
Query:

ALTER TABLE Sales
ADD CONSTRAINT fk_product_id
FOREIGN KEY (product_id)
REFERENCES Products(product_id);
Output:

No output is generated, but the constraint is applied to the table.
Explanation:

This query adds a foreign key constraint to the Sales table that references the product_id column in the Products table, ensuring referential integrity between the two tables.

5. Create a view named Top_Products that lists the top 3 products based on the total quantity sold.
Query:

CREATE VIEW Top_Products AS
SELECT p.product_name, SUM(s.quantity_sold) AS total_quantity_sold
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 3;
Output:

product_name	total_quantity_sold
Mouse	6
Laptop	5
Keyboard	4
Explanation:

This query creates a view named Top_Products that lists the top 3 products based on the total quantity sold.

6. Implement a transaction that deducts the quantity sold from the Products table when a sale is made in the Sales table, ensuring that both operations are either committed or rolled back together.
Query:

START TRANSACTION; -- Begin the transaction

-- Deduct the quantity sold from the Products table
UPDATE Products p
JOIN Sales s ON p.product_id = s.product_id
SET p.quantity_in_stock = p.quantity_in_stock - s.quantity_sold;

-- Check if any negative quantities would result from the update
SELECT COUNT(*) INTO @negative_count
FROM Products
WHERE quantity_in_stock < 0;

-- If any negative quantities would result, rollback the transaction
IF @negative_count > 0 THEN
    ROLLBACK;
    SELECT 'Transaction rolled back due to insufficient stock.' AS Message;
ELSE
    COMMIT; -- Commit the transaction if no negative quantities would result
    SELECT 'Transaction committed successfully.' AS Message;
END IF;

START TRANSACTION;
UPDATE Products SET quantity_in_stock = 10 WHERE product_id = 101;
INSERT INTO Sales (product_id, quantity_sold) VALUES (101, 5);
COMMIT;
Output:

Transaction committed successfully.
Explanation:

The quantity in stock for product with product_id 101 should be updated to 5.The transaction should be committed successfully.

7. Create a query that lists the product names along with their corresponding sales count.
Query:

SELECT p.product_name, COUNT(s.sale_id) AS sales_count
FROM Products p
LEFT JOIN Sales s ON p.product_id = s.product_id
GROUP BY p.product_name;
Output:

product_name	sales_count
Headphones	1
Keyboard	1
Laptop	1
Mouse	1
Smartphone	1
Explanation:

This query selects the product names from the Products table and counts the number of sales (using the COUNT() function) for each product by joining the Sales table on the product_id. The results are grouped by product name using the GROUP BY clause.

8. Write a query to find all sales where the total price is greater than the average total price of all sales.
Query:

SELECT *
FROM Sales
WHERE total_price > (SELECT AVG(total_price) FROM Sales);
Output:

sale_id	product_id	quantity_sold	sale_date	total_price
1	101	5	2024-01-01	2500.00
2	102	3	2024-01-02	900.00
Explanation:

The subquery (SELECT AVG(total_price) FROM Sales) calculates the average total price of all sales. The main query selects all columns from the Sales table where the total price is greater than the average total price obtained from the subquery.

9. Analyze the performance implications of indexing the sale_date column in the Sales table, considering the types of queries commonly executed against this column.
Query:

-- Query without indexing
EXPLAIN ANALYZE
SELECT *
FROM Sales
WHERE sale_date = '2024-01-01';

-- Query with indexing
CREATE INDEX idx_sale_date ON Sales (sale_date);

EXPLAIN ANALYZE
SELECT *
FROM Sales
WHERE sale_date = '2024-01-01';
Output:

Query without Indexing:
Operation	Details
Filter: (sales.sale_date = DATE’2024-01-01′)	(cost=0.75 rows=1) (actual time=0.020..0.031 rows=1 loops=1)
Table scan on Sales	(cost=0.75 rows=5) (actual time=0.015..0.021 rows=5 loops=1)
Query with Indexing:
Operation	Details
Index lookup on Sales using idx_sale_date (sale_date=DATE’2024-01-01′)	(cost=0.35 rows=1) (actual time=0.024..0.024 rows=1 loops=1)
This format clearly displays the operations and details of the query execution plan before and after indexing.

Explanation:

Without indexing, the query performs a full table scan, filtering rows based on the sale date, which is less efficient. With indexing, the query uses the index to quickly locate the relevant rows, significantly improving query performance.

10. Add a check constraint to the quantity_sold column in the Sales table to ensure that the quantity sold is always greater than zero.
Query:

ALTER TABLE Sales
ADD CONSTRAINT chk_quantity_sold CHECK (quantity_sold > 0);

-- Query to check if the constraint is applied successfully
SELECT * FROM Sales;
Output:

sale_id

product_id

quantity_sold

sale_date

total_price

1

101

5

2024-01-01

2500.00

2

102

3

2024-01-02

900.00

3

103

2

2024-01-02

60.00

4

104

4

2024-01-03

80.00

5

105

6

2024-01-03

90.00

Explanation:

All rows in the Sales table meet the condition of the check constraint, as each quantity_sold value is greater than zero.

11. Create a view named Product_Sales_Info that displays product details along with the total number of sales made for each product.
Query:

CREATE VIEW Product_Sales_Info AS
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    p.unit_price,
    COUNT(s.sale_id) AS total_sales
FROM 
    Products p
LEFT JOIN 
    Sales s ON p.product_id = s.product_id
GROUP BY 
    p.product_id, p.product_name, p.category, p.unit_price;
Output:

product_id	product_name	category	unit_price	total_sales
101	Laptop	Electronics	500.00	1
102	Smartphone	Electronics	300.00	1
103	Headphones	Electronics	30.00	1
104	Keyboard	Electronics	20.00	1
105	Mouse	Electronics	15.00	1
Explanation:

This view provides a concise and organized way to view product details alongside their respective sales information, facilitating analysis and reporting tasks.

12. Develop a stored procedure named Update_Unit_Price that updates the unit price of a product in the Products table based on the provided product_id.
Query:

DELIMITER //

CREATE PROCEDURE Update_Unit_Price (
    IN p_product_id INT,
    IN p_new_price DECIMAL(10, 2)
)
BEGIN
    UPDATE Products
    SET unit_price = p_new_price
    WHERE product_id = p_product_id;
END //

DELIMITER ;
Output:

There is no direct output shown here as this is a stored procedure definition
Explanation:

The above SQL code creates a stored procedure named Update_Unit_Price. This stored procedure takes two parameters: p_product_id (the product ID for which the unit price needs to be updated) and p_new_price (the new unit price to set).

13. Implement a transaction that inserts a new product into the Products table and then adds a corresponding sale record into the Sales table, ensuring that both operations are either fully completed or fully rolled back.
Query:

CREATE PROCEDURE Update_Unit_Price (
    @product_id INT,
    @new_unit_price DECIMAL(10, 2)
)
AS
BEGIN
    UPDATE Products
    SET unit_price = @new_unit_price
    WHERE product_id = @product_id;
END;

EXEC Update_Unit_Price @product_id = 101, @new_unit_price = 550.00;
SELECT * FROM Products;
Output:

product_id

product_name

category

unit_price

101

Laptop

Electronics

550.00

102

Smartphone

Electronics

300.00

103

Headphones

Electronics

30.00

104

Keyboard

Electronics

20.00

105

Mouse

Electronics

15.00

Explanation:

This will update the unit price of the product with product_id 101 to 550.00 in the Products table.

14. Write a query that calculates the total revenue generated from each category of products for the year 2024.
Query:

SELECT 
    p.category,
    SUM(s.total_price) AS total_revenue
FROM 
    Sales s
JOIN 
    Products p ON s.product_id = p.product_id
WHERE 
    strftime('%Y', s.sale_date) = '2024'
GROUP BY 
    p.category;
Output:

category

total_revenue

Electronics

3630.00

Explanation:

When you execute this query, you will get the total revenue generated from each category of products for the year 2024.
