
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
