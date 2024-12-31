SELECT * 
FROM Sales;

SELECT Product, SUM(Price * Quantity) AS TotalRevenue 
FROM Sales 
GROUP BY Product;

SELECT Max(Price)
FROM Sales;

SELECT * 
FROM Sales
WHERE OrderDate = '2024-12-29';
