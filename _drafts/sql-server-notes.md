
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
- recommended by Microsoft to use `THROW`
- syntax: `THROW [error_number, message, state] [;]`
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
#### Customizing error messages
2 ways:
- variable by concatenated strings
```SQL
DECLARE @first_name NVARCHAR(20) = 'Pedro';
-- Concat the message
DECLARE @my_message NVARCHAR(500) =
	CONCAT('There is no staff member with ', @first_name, ' as the first name.');

IF NOT EXISTS (SELECT * FROM staff WHERE first_name = @first_name)
	-- Throw the error
	THROW 50000, @my_message, 1;
```
- `FROMATMESSAGE` function
```SQL
DECLARE @product_name AS NVARCHAR(50) = 'Trek CrossRip+ - 2018';
DECLARE @number_of_sold_bikes AS INT = 10;
DECLARE @current_stock INT;
-- Select the current stock
SELECT @current_stock = stock FROM products WHERE product_name = @product_name;
DECLARE @my_message NVARCHAR(500) =
	-- Customize the message
	FORMATMESSAGE('There are not enough %s bikes. You only have %d in stock.', @product_name, @current_stock);

IF (@current_stock - @number_of_sold_bikes < 0)
	-- Throw the error
	THROW 50000, @my_message, 1;
```

### Transactions and Error Handling
- `BEGIN TRAN|TRANSACTION` marks the starting point of a transaction.
- `COMMIT TRAN|TRANSACTION` marks the end of a successful transaction.
- `ROLLBACK TRAN|TRANSACTION` reverts transaction to the beginning or a savepoint inside the transaction.
using ROLLBACK when there is an error:
```SQL
BEGIN TRY  
	BEGIN TRAN;
		UPDATE accounts SET current_balance = current_balance - 100 WHERE account_id = 1;
		INSERT INTO transactions VALUES (1, -100, GETDATE());

		UPDATE accounts SET current_balance = current_balance + 100 WHERE account_id = 5;
		INSERT INTO transactions VALUES (5, 100, GETDATE());
	COMMIT TRAN;
END TRY
BEGIN CATCH  
	ROLLBACK TRAN;
END CATCH
```
This example; give accounts less than $5000 and extra $100 but only if there is less than 20 accounts
```SQL
-- Begin the transaction
BEGIN TRANSACTION;
	UPDATE accounts set current_balance = current_balance + 100
		WHERE current_balance < 5000;
	-- Check number of affected rows
	IF @@ROWCOUNT > 20
		BEGIN
        	-- Rollback the transaction
			ROLLBACK TRAN;
			SELECT 'More accounts than expected. Rolling back';
		END
	ELSE
		BEGIN
        	-- Commit the transaction
			COMMIT TRAN;
			SELECT 'Updates commited';
		END
```

#### @@TRANCOUNT
- `@@TRANCOUNT` keeps count of the number of transactions.
- - `BEGIN TRAN` increments `@@TRANCOUNT` +1
- - `COMMIT TRAN` decrements `@@TRANCOUNT` -1
- - `ROLLBACK TRAN` decrements `@@TRANCOUNT` to 0 unless there is a save point.
```SQL
BEGIN TRY
	-- Begin the transaction
	BEGIN TRAN;
    	-- Correct the mistake
		UPDATE accounts SET current_balance = current_balance + 200
			WHERE account_id = 10;
    	-- Check if there is a transaction
		IF @@TRANCOUNT > 0     
    		-- Commit the transaction
			COMMIT TRAN;

	SELECT * FROM accounts
    	WHERE account_id = 10;      
END TRY
BEGIN CATCH  
    SELECT 'Rolling back the transaction';
    -- Check if there is a transaction
    IF @@TRANCOUNT > 0   	
    	-- Rollback the transaction
        ROLLBACK TRAN;
END CATCH
```

#### Savepoints
- save current 'safe' state which to rollback to.
- syntax: `SAVE TRAN|TRANSACTION <savepoint_name|@savepoint_variable`>;
- to rollback to a savepoint: `ROLLBACK TRAN?TRANSACTION <savepoint_name|@savepoint_variable>;`
```SQL
BEGIN TRAN;
	-- Mark savepoint1
	SAVE TRAN savepoint1;
	INSERT INTO customers VALUES ('Mark', 'Davis', 'markdavis@mail.com', '555909090');

	-- Mark savepoint2
    SAVE TRAN savepoint2;
	INSERT INTO customers VALUES ('Zack', 'Roberts', 'zackroberts@mail.com', '555919191');

	-- Rollback savepoint2
	ROLLBACK TRAN savepoint2;
    -- Rollback savepoint1
	ROLLBACK TRAN savepoint1;

	-- Mark savepoint3
	SAVE TRAN savepoint3;
	INSERT INTO customers VALUES ('Jeremy', 'Johnsson', 'jeremyjohnsson@mail.com', '555929292');
-- Commit the transaction
COMMIT TRAN;
```

#### XACT_ABORT and XACT_
XACT_ABORT
- specify if current transaction should be automatically rolledback (aborted) if error occurs.
- default setting is off
- - if there are errors, there can be open transactions.
- `SET XACT_ABORT ON` - if there's an error, rollbacks the tranaction and aborts the execution.
- better to use `THROW` to throw an error, and activate `XACT_ABORT`.
- - `RAISE_ERROR()` will warn about the error, but won't activate `XACT_ABORT`
```SQL
-- Use the appropriate setting
SET XACT_ABORT ON;
-- Begin the transaction
BEGIN tran;
	UPDATE accounts set current_balance = current_balance - current_balance * 0.01 / 100
		WHERE current_balance > 5000000;
	IF @@ROWCOUNT <= 10
    	-- Throw the error
		THROW 50000, 'Not enough wealthy customers!', 1;
	ELSE		
    	-- Commit the transaction
		COMMIT tran;
```
XACT_STATE
- `0` no open transactions
- `1` open and commitable transactions
- `-1` open and uncommitable transaction (doomed transaction)
- - can't commit
- - can't rollback to a savepoint
- - can rollback the full transaction
- - can't make any changes/can read data
```SQL
SET XACT_ABORT ON;
BEGIN TRY
  BEGIN TRAN;
    INSERTINTO customers VALUES ('Mark', 'Davis', 'markdavis@mail.com', '555909090');
    INSERTINTO customers VALUES ('Dylan', 'Smith', 'dylansmith@mail.com', '555888999'); -- ERROR!
  COMMIT TRAN;
END TRY
BEGIN CATCH
  IF XACT_STATE() = -1
    ROLLBACK TRAN;
  IF XACT_STATE() = 1
    COMMIT TRAN;
  SELECT ERROR_MESSAGE() AS Error_message;
END CATCH
```

### Controlling concurrency: transaction isolation levels

- Phantom reads occur when a transaction reads some records twice, but the first result it gets is different from the second result as a consequence of another committed transaction having inserted a row.

transction isolation levels:
- `READ COMMITTED` default
- `READ UNCOMMITTED`
- - least restrictive isolation level
- - read rows from another transaction which has not been committed/rolledback yet.
- `REPEATABLE READ`
- `SERIALIZABLE`
- `SNAPSHOT`
- syntax: `SET TRANSACTION ISOLATION ISOLATION LEVEL READ UNCOMMITTED`

knowing current isolation level:
```SQL
SELECT CASE transaction_isolation_level
    WHEN 0 THEN 'UNSPECIFIED'
    WHEN 1 THEN 'READ UNCOMMITTED'
    WHEN 2 THEN 'READ COMMITTED'
    WHEN 3 THEN 'REPEATABLEREAD'
    WHEN 4 THEN 'SERIALIZABLE'
    WHEN 5 THEN'SNAPSHOT'
  END AS transaction_isolation_level FROM sys.dm_exec_sessions
WHERE session_id = @@SPID
```

`READ UNCOMMITTED` summary
Pro:
- can be faster, doesn't block other transactions
Con:
- allows dirty reads, non-repeatable reads, and phantom reads
when to use:
- dno't want to be blocked by other transactions, and don't mind concurrency phenomena
- explicitly want to watch uncommitted data

`READ COMMITTED`
- default isolation level
- cant read data that has not been committed or rollbacked
- syntax `SET TRANSACTION ISOLATION LEVEL READ COMMITTED`
- prevents "dirty reads", but doesn't prevent non-repeatable reads and phantom reads

`REPEATABLE READ`
- can't read uncommitted data from other transactions
- while reading data other transactions can't modify the data until `REPEATABLE READ` transaction completes.
- does not prevent phantom reads

`SERIALIZABLE`
- most restrictibe isolation level
- prevents dirty, non-repeatable and phantom reads
- if `SERIALIZABLE READ` is on and index, then only that records are locked.
- if `SERIALIZABLE READ` is not on index, the whole table is locked.

`SNAPSHOT`
-`ALTER DATABASE myDatabaseName SET ALLOW_SNAPSHOT_ISOLATION ON` and `ALTER DATABASE myDatabaseName SET READ_COMMITTED_SNAPSHOT ON`

- The `WITH (NOLOCK)`` option behaves like the `READ UNCOMMITTED` isolation level. But whereas the isolation level applies for the entire connection, WITH NOLOCK applies to a specific table.
