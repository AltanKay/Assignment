SELECT SUM(Price * Quantity) AS TotalRevenue FROM Sales;


--Most popular product:
SELECT Product, SUM(Quantity) AS TotalQuantitySold
FROM Sales
GROUP BY Product
ORDER BY TotalQuantitySold DESC
LIMIT 1;

--OR--
SELECT Product, MAX(TotalQuantitySold) AS MostPopularProduct
FROM (
    SELECT Product, SUM(Quantity) AS TotalQuantitySold
    FROM Sales
    GROUP BY Product
) AS Subquery;
--other option to be studied--
SELECT Product, SUM(Quantity) AS TotalQuantitySold
FROM Sales
GROUP BY Product
HAVING TotalQuantitySold > 30;


SELECT AVG(Price) AS AveragePrice
FROM Sales;

--total number of unique products:
SELECT COUNT(DISTINCT Product) AS TotalUniqueProducts
FROM Sales;

--The product with the highest revenue:
SELECT Product, SUM(Price * Quantity) AS TotalRevenue
FROM Sales
GROUP BY Product
ORDER BY TotalRevenue DESC
LIMIT 1;

 