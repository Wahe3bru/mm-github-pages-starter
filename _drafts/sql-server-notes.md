
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

variables must start with `@` followed by data type.
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
SET @listened = 20

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
