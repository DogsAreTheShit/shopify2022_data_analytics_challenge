# Zane Chiang takes on the Shopify 2022 Data Analytics Challenge!

## Question 1:
  ASK: Calculate an AOV for a 30 day window

### a) What could go wrong?
  When creating a program to calculate an AOV for a 30 day window, I too first went to the simple solution of calculating the mean for the column using pandas libraries and naively calculated ~$3,145. Upon further inspection, I discovered 20 records with abnormal order amounts of ~$700,000. These being statistical outliers, I decided to handle these abnormalities by removing any records which fall outside of 3 standard deviations. This gave me a much more reasonable value of $723.26!
### b) What metric would you report for this dataset?
  Adjusted AOV

### c) What is its value?
  $723.26


## Question 2:

### a) How many orders were shipped by Speedy Express in total?
  SQL Query:
  <SELECT COUNT(OrderID) FROM Orders AS o, Shippers AS s WHERE o.ShipperID = s.ShipperID AND s.ShipperName = "Speedy Express";>

  Result: 
  54

### b) What is the last name of the employee with the most orders?
SQL Query:
<SELECT LastName FROM (SELECT e.EmployeeID, LastName, Count(OrderID) AS Num_Orders FROM Employees as e, Orders as o WHERE e.EmployeeID = o.EmployeeID GROUP BY o.EmployeeID ORDER BY Num_Orders DESC LIMIT 1);>

  Result: 
  Peacock
### c) What product was ordered the most by customers in Germany?
SQL Query:
<SELECT ProductName, SUM(Quantity) as NumOrders FROM Orders as o, Customers as c, OrderDetails as od, Products as p WHERE c.CustomerID=o.CustomerID AND c.Country = "Germany" AND o.OrderID = od.OrderID AND p.productID = od.productID GROUP BY p.ProductID ORDER BY NUmOrders Desc LIMIT 1;>

  Result:
  Boston Crab Meat

