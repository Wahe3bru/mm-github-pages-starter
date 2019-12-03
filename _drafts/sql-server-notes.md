
get the top to results (limit to 20)
```sql
SELECT
    TOP (20) names
FROM
    countries
```
get the top half (50%) of a table
```SQL
SELECT
    TOP (50) PERCENT *
FROM
    countries
```

When aggregating data always alias columns

CHARINDEX(<chars>, <column>) to return index of char/s

```SQL
-- UPDATE the title of the album
UPDATE
  album
SET
  title = 'Pure Cult: The Best Of The Cult'
WHERE
  album_id = 213;
```

### Variables
create variable: `DECLARE @test_int INT` or `DECLARE @my_artist(VARCHAR(100))`
assign value to variable: `SET @test_int = 5` or `SET @my_artist = 'Lupe Fiasco'`

variables must start with `@` followed by data type.<br>
__variable datatypes__
- `VARCHAR(n)`
- `INT`
- `DECIMAL(p, s)` or `NUMERIC(p, s)`:
- - `p`: total number of digits that will be stored, both to the left and right of the decimal.
- - `s`: number of digits to the right of the decimal point.

```SQL
DECLARE @my_artist VARCHAR(50)
DECLARE @listened INT

SET @my_artist = 'Lupe Fiasco'
-- alternatively, can use SELECT
SELECT @listened = 20

SELECT
    track_name, album
FROM
    songs
WHERE
    artist = @my_artist
  AND
    plays >= @listened
-- save into temp table
INTO fave_artist_temp_table
```

### WHILE loops
- `WHILE` evaluates a true or false condition
- after the WHILE, there should be a `BEGIN` line
- after the code, end with keyword `END`
- `BREAK` will exit the loop
- `CONTINUE` will cause the loop to continue

```SQL
DECLARE @counter INT
SET @counter = 20
-- Create a loop
WHILE @counter < 30
-- Loop code starting point
BEGIN
	SELECT @counter = @counter + 1
  -- if @counter reaches 27 break out of loop
  IF @counter = 27
      BREAK
-- Loop finish
END
-- Check the value of the variable
SELECT @counter
```


### Derived Tables
- Query treated like a temporary table
- Always contained within the main query
- It's specified in the `FROM` clause
- can contain intermediate calculations to be used in main query or different joins than in the main query

```SQL
SELECT a.*
FROM Kidney a
-- Derived table computes average age joined to actual table
JOIN (SELECT AVG(Age) AS AverageAge
      FROM kidney) b
  ON a.Age = b.AverageAge
```

### (CTE) Common Table Expression
- a more advance derived table,
- create a table that will be used in succeding query
- can be used multiple times.
- `WITH` <cte_name> (col1, col2, etc) `AS` (<query that selects columns)
- - query must return the columns in cte_name
```SQL
-- Specify the keyowrds to create the CTE
WITH BloodGlucoseRandom (MaxGlucose)
AS (SELECT MAX(BloodGlucoseRandom) AS MaxGlucose FROM Kidney)

SELECT a.Age, b.MaxGlucose
FROM Kidney a
-- Join the CTE on blood glucose equal to max blood glucose
JOIN BloodGlucoseRandom b
ON a.BloodGlucoseRandom = b.MaxGlucose
```

### Window Functions
Allows aggregations to be created at the same time as the window.<br>
Window syntax in T-SQL
- Create window with `OVER` clause
- `PARTITION BY` creates the frame
- - if left out frame is the entire table
- `ORDER BY` to arrange results
```SQL
SELECT OrderID, TerritoryName,
       -- Total price for each partition
       SUM(OrderPrice)
       -- Create the window and partitions
       OVER(PARTITION BY TerritoryName) AS TotalPrice
FROM Orders
```
#### Common Window functions
`ORDER BY` must be used to get the correct value for these functions
- `FIRST_VALUE`
```SQL
SELECT Area, OrderDate
       -- select first value in each partition
       FIRST_VALUE(OrderDate)
       OVER(PARTITION BY Area ORDER BY OrderDate) AS FirstOrder
FROM Orders
```
- `LAST_VALUE`
- `LEAD`
- `LAG`
```sql
SELECT TerritoryName, OrderDate,
       -- Specify the previous OrderDate in the window
       LAG(OrderDate)
       -- Over the window, partition by territory & order by order date
       OVER(PARTITION BY TerritoryName ORDER BY OrderDate) AS PreviousOrder,
       -- Specify the next OrderDate in the window
       LEAD(OrderDate)
       -- Create the partitions and arrange the rows
       OVER(PARTITION BY TerritoryName ORDER BY OrderDate) AS NextOrder
FROM Orders
```

## Transactions and Error Handling in SQL Server
```sql
BEGIN TRY
    -- attempt code  here
END TRY
BEGIN CATCH
    --- code here if above failed
END CATCH
```
nested try and catch:
```sql
BEGIN TRY
    -- attempt code  here
END TRY
BEGIN CATCH
    --- code here if above failed
    BEGIN TRY
        -- 2nd attempt code  here
    END TRY
    BEGIN CATCH
        --- code here if above failed
    END CATCH
END CATCH
```
#### Anatomy of an error message
```bash
# 1         2         3          4
Msg 2627, Level 14, State 1, Line 1
Violation of UNIQUE KEY constraint 'unique_name'.
Cannot insert duplicate key in object 'dbo.products'.
The duplicate key value is (Trek Powerfly 5 - 2018).
```
1. error number
- SQL errors: 1 to 49999
- Own errors: starting from 50001

2. severity Level
- 0-10: informational messages
- 11-16: errors that can be corrected by the user (constraint violation, etc.)
- 17-24: other errors (software problems,fatal errors)

3. State
- 1: if SQL Server displays error
- 0-255: own errors

4. Line number , and if procedure/function name<br>

**Uncatchable errors**
- Severity lower than 11 (11-19 are catchable)
- Severity of 20 or higher that stop the connection
- Compilation errors: objects and columns that don't exist

#### Get information about errors
- when using TRY/CATCH block we lose info about the error
- error functions
- - `ERROR_NUMBER()` returns the number ofthe error.
- - `ERROR_SEVERITY()` returns the error severity (11-19).
- - `ERROR_STATE()` returns the state ofthe error.
- - `ERROR_LINE()` returns the number ofthe line ofthe error.
- - `ERROR_PROCEDURE()` returns the name of stored procedure/trigger. NULL ifthere is not storedprocedure/trigger.
- - `ERROR_MESSAGE()` returns the text ofthe error message.
- These functions must be placed within the CATCH block. If an error occurs within the TRY block, they return information about the error.
```sql
BEGIN TRY
  INSERT INTO products (product_name, stock, price)
  VALUES ('Trek Powerfly 5 - 2018', 10, 3499.99);
END TRY
BEGIN CATCH
  SELECT
    ERROR_NUMBER() AS Error_number,
    ERROR_SEVERITY() AS Error_severity,
    ERROR_STATE() AS Error_state,
    ERROR_PROCEDURE() AS Error_procedure,
    ERROR_LINE() AS Error_line,
    ERROR_MESSAGE() AS Error_message;
END CATCH
```
#### THROW
- using `THROW` without parameters re-throws an error
- you can catch error thrown in stored procedure and get error message
```SQL
BEGIN TRY
	-- Execute the stored procedure
	EXEC insert_products
    	-- Set the values for the parameters
    	@product_name = 'Super bike',
        @stock = 3,
        @price = 499.99;
END TRY
-- Set up the CATCH block
BEGIN CATCH
	-- Select the error message
	SELECT ERROR_MESSAGE();
END CATCH
```
- THROW errors with parameters
```SQL
-- Set @staff_id to 4
DECLARE @staff_id INT = 4;

IF NOT EXISTS (SELECT * FROM staff WHERE staff_id = @staff_id)
   	-- Invoke the THROW statement with parameters
	THROW 50001, 'No staff member with such id', 1;
ELSE
   	SELECT * FROM staff WHERE staff_id = @staff_id
```
