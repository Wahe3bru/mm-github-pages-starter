
#### Chapter 1 - 4:
- [x] Overview and light reading                        6/11/2019

## Section II - Structure APIs
### Structured API Overview
- [x] DataFrames and Datasets
- [x] Schemas
- [x] Overview of Structured Spark Types
- - [x] DataFrames vs Datasets
- - [x] Columns
- - [x] Rows
- - [x] SparkTypes
- Overview of Structured API Execution
- - [x] Logical Planning
- - [x]  Physical Planning
- - [x] Execution

### Basic Structured Operations
- [x] Schemas
- [x]  Columns and Expressions
- - [x] Columns
- - [x] Expressions
- [x] Records and Rows
- - [x] Creating Rows
- [x] DataFrame transformations
- - [x] Creating DataFrames
- - [x] select and selectExpr
- - [x] Converting to Spark Types (Literals)
- - [x] Adding Columns
- - [x] Renaming Columns
- - [x] Reserved Characters and Keywords
- - [x] Case Sensitivity
- - [x] Removing Columns
- - [x] Changing Column's Type (cast)                      7/11/2019
- - [x] Filtering Rows
- - [x] Getting Unique Rows
- - [x] Random Samples
- - [x] Random Splits
- - [x] Concatenating and Appending Rows (Union)
- - [x] Sorting Rows
- - [x]  Limit
- - [x] Repartition and Coalesce
- - [x] Collecting Rows to the Driver                       8/11/2019

### Working with different types of data
- [x] Where to look for APIs
- [x] Converting to SparkTypes
- [x] Working with Booleans
- [x] Working with Numbers
- [x] Working with Strings                                   11/11/2019
- - [x] Regular Expressions
- [x] Working with Dates and Timestamps                      12/11/2019
- [x] Working with Nulls in data
- - [x] Coalesce
- - [x] ifnull, nullifm nvl, and nvl2
- - [x] drop
- - [x] fill
- - [x] replace
- [x] Ordering                                                14/11/2019
- [ ] Working with Complex Types
- - [ ] Structs
- - [ ] Arrays
- - [ ] split
- - [ ] Array Length
- - [ ] array_contains
- - [ ] explode
- - [ ] Maps
- [ ] Working with JSON
- [x] User-Defined Functions

### Aggregations
- [x] Aggregations Functions
- - [x] count
- - [x] countDistinct
- - [x] approx_count_distict
- - [x] first and last
- - [x] min and max
- - [x] sum
- - [x] sumDisctint
- - [x] avg
- - [x] Variance and Standard Deviation
- - [x] skewness and kurtosis
- - [x] Covariance and Correlation
- - [x] Aggregating to Complex Types
- [x] Grouping
- - [x] Grouping with Expressions
- - [x] Grouping with Maps                                 20/11/2019
- [x] Window Functions
- [x] Grouping Sets
- - [x] Rollups
- - [x] Cube
- - [x] Grouping Metadata
- - [x] Pivot
- [x] User-Defined Aggregation Functions                    21/11/2019

### Joins
- [x] Join Expressions
- [x] Join Types
- [x] Inner Joins
- [x] Outer Joins
- [x] Left Outer Joins
- [x] Right Outer Joins
- [x] Left Semi Joins
- [x] Left Anti Joins
- [x] Natural Joins
- [x] Cross (Cartesian) Joins
- [x] Challenges when using Joins
- - [x] Joins on Complex Types
- - [x] Handling Duplicate Column Names
- [x] How Spark performs Joins
- - [x] Communications strategies                           26/11/2019

### Data Sources
- [ ] Structure of Data Sources API
- - [ ] Read API Structure
- - [ ] Basics of Reading Data
- - [ ] Write API Structure
- - [ ] Basics of Writing Data
- [ ] CSV Files
- - [ ] CSV Options
- - [ ] Reading csv
- - [ ] Writing csv
- [ ] JSON Files
- - [ ] json Options
- - [ ] Reading json
- - [ ] Writing json
- [ ] Parquet Files
- - [ ] Reading Parquet
- - [ ] Writing Parquet
- [ ] ORC Files
- - [ ] Reading Orc
- - [ ] Writing Orc
- [ ] SQL Databases
- - [ ] Reading from SQL databases
- - [ ] Query Pushdown
- - [ ] Writing to SQL databases
- [ ] Text Files
- - [ ] Reading Text
- - [ ] Writing Text
- [ ] Advanced I/O Concepts
- - [ ] Splitting File Types and Compression
- - [ ] Reading data in Parallel
- - [ ] Writing data in Parallel
- - [ ] Writing Complex Types
- - [ ] Managing File Size

### Spark SQL
- [x] Big Data and SQL: Apache Hive
- [x] Big Data and SQL: Spark SQL
- - [x] Spark’s Relationship to Hive
- [x] How to Run Spark SQL Queries
- - [x] Spark SQL CLI
- - [x] Spark’s Programmatic SQL Interface
- - [x] SparkSQL Thrift JDBC/ODBC Server
- [x] Catalog
- [x] Tables
- - [x] Spark-Managed Tables
- - [x] Creating Tables
- - [x] Creating External Tables
- - [x] Inserting into Tables
- - [x] Describing Table Metadata
- - [x] Refreshing Table Metadata
- - [x] Dropping Tables
- - [x] Caching Tables
- [x] Views
- - [x] Creating Views
- - [x] Dropping Views
- [x] Databases
- - [x] Creating Databases
- - [x] Setting the Database
- - [x] Dropping Databases
- [x] Select Statements
- - [x] case…when…then Statements
- [x] Advanced Topics
- - [x] Complex Types
- - [x] Functions
- - [x] Subqueries
- [x] Miscellaneous Features
- - [x] Configurations
- - [x] Setting Configuration Values in SQL               25/11/2019

### Datasets
### Resilient Distributed Datasets (RDDs)
### Advanced RDDs
### Distributed Shared Variables

## Section IV - Production Applications
### How Spark Runs on a Cluster
### Developing Spark Applications
### Deploying Spark
### Monitoring and Debugging
### Performance Tuning

## Section V - Streaming
### Stream Processing Fundamentals
### Structured Streaming Basics
### Event-Time and Stateful Processing
### Structured Streaming in Production

## Section VI - Advanced Analytics and Machine Learning
### Advanced Analytics and Machine Learning Overview
- [ ] A Short Primer on Advanced Analytics
- - [ ] Supervised Learning
- - [ ] Recommendation
- - [ ] Unsupervised Learning
- - [ ] Graph Analytics
- - [ ] The Advanced Analytics Process
- [ ] Spark’s Advanced Analytics Toolkit
- - [ ] What Is MLlib?
- [ ] High-Level MLlib Concepts
- [ ] MLlib in Action
- - [ ] Feature Engineering with Transformers
- - [ ] Estimators
- - [ ] Pipelining Our Workflow
- - [ ] Training and Evaluation
- - [ ] Persisting and Applying Models
- [ ] Deployment Patterns

### Preprocessing and Feature Engineering
- [ ] Formatting Models According to Your Use Case
- [ ] Transformers
- [ ] Estimators for Preprocessing
- - [ ] Transformer Properties
- [ ] High-Level Transformers
- - [ ] RFormula
- - [ ] SQL Transformers
- - [ ] VectorAssembler
- [ ] Working with Continuous Features
- - [ ] Bucketing
- - [ ] Scaling and Normalization
- - [ ] StandardScaler
- [ ] Working with Categorical Features
- - [ ] StringIndexer
- - [ ] Converting Indexed Values Back to Text
- - [ ] Indexing in Vectors
- - [ ] One-Hot Encoding
- [ ] Text Data Transformers
- - [ ] Tokenizing Text
- - [ ] Removing Common Words
- - [ ] Creating Word Combinations
- - [ ] Converting Words into Numerical Representations
- - [ ] Word2Vec
- [ ] Feature Manipulation
- - [ ] PCA
- - [ ] Interaction
- - [ ] Polynomial Expansion
- [ ] Feature Selection
- - [ ] ChiSqSelector
- [ ] Advanced Topics
- - [ ] Persisting Transformers
- [ ] Writing a Custom Transformer

### Classification
- [ ] Use Cases
- [ ] Types of Classification
- - [ ] Binary Classification
- - [ ] Multiclass Classification
- - [ ] Multilabel Classification
- [ ] Classification Models in MLlib
- - [ ] Model Scalability
- [ ] Logistic Regression
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Prediction Parameters
- - [ ] Example
- - [ ] Model Summary
- [ ] Decision Trees
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Prediction Parameters
- [ ] Random Forest and Gradient-Boosted Trees
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Prediction Parameters
- [ ] Naive Bayes
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Prediction Parameters
- [ ] Evaluators for Classification and Automating Model Tuning
- [ ] Detailed Evaluation Metrics
- [ ] One-vs-Rest Classifier
- [ ] Multilayer Perceptron

### Regression
- [ ] Use Cases
- [ ] Regression Models in MLlib
- - [ ] Model Scalability
- [ ] Linear Regression
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Example
- - [ ] Training Summary
- [ ] Generalized Linear Regression
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Prediction Parameters
- - [ ] Example
- - [ ] Training Summary
- [ ] Decision Trees
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Example
- [ ] Random Forests and Gradient-Boosted Trees
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Example
- [ ] Advanced Methods
- - [ ] Survival Regression (Accelerated Failure Time)
- - [ ] Isotonic Regression
- [ ] Evaluators and Automating Model Tuning
- [ ] Metrics

### Recommendation
- [ ] Use Cases
- [ ] Collaborative Filtering with Alternating Least Squares
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Prediction Parameters
- - [ ] Example
- [ ] Evaluators for Recommendation
- [ ] Metrics
- - [ ] Regression Metrics
- - [ ] Ranking Metrics
- [ ] Frequent Pattern Mining

### Unsupervised Learning
- [ ] Use Cases
- [ ] Model Scalability
- [ ] k-means
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Example
- - [ ] k-means Metrics Summary
- [ ] Bisecting k-means
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Example
- - [ ] Bisecting k-means Summary
- [ ] Gaussian Mixture Models
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Example
- - [ ] Gaussian Mixture Model Summary
- [ ] Latent Dirichlet Allocation
- - [ ] Model Hyperparameters
- - [ ] Training Parameters
- - [ ] Prediction Parameters
- - [ ] Example

### Graph Analytics
- [ ] Building a Graph
- [ ] Querying the Graph
- - [ ] Subgraphs
- [ ] Motif Finding
- [ ] Graph Algorithms
- - [ ] PageRank
- - [ ] In-Degree and Out-Degree Metrics
- - [ ] Breadth-First Search
- - [ ] Connected Components
- - [ ] Strongly Connected Components
- - [ ] Advanced Tasks

### Deep Learning

## Section VII - Ecosystem
### Language Specifics: Python (PySpark) and R (SparkR and sparklyr)
- [ ] PySpark
- - [ ] Fundamental PySpark Differences
- - [ ] Pandas Integration

### Ecosystem and Community

---
## Notes
### Structured API Overview

__Schemas__<br>
- defines column names and data types of a dataframe.
- schemas can be defined manually or inferred automatically (_schema on read_)

__dataframes and datasets__
- datasets are only available to java-based languages (Scala or Java)
- dataframes are what all other interpreted languages used. The cool thing about that is that what language used, python or r, the actual work done is spark using the __catalyst__ engine.
- dataframes make use of Sparks optimized internal format

__spark types__
To work with correct  Python types, they can be accessed by `from pyspark.sql.types import *`
some common Python type reference:

Data type | Value type in Python | API
---|---|---
ByteType | int 1byte integer -128 to 127 |ByteType()
LongType | long best practice for integer | LongType()
FloatType | float | FloatType()
DoubleType | float | DoubleType()
DecimalType | decimal.Decimal | DecimalType()
StringType | string | StringType()
BinaryType | bytearray | BinaryType()
BooleanType | bool | BooleanType()
TimestampType | datetime.datetime | TimestampType()
DateType | datetime.date | DateType()
MapType | dict | MapType(keyType, valueType, [valueContainsNull])
StructType | list or tuple |*StructType(fields). Note: fields is a list of StructFields. Also, fields with the same name are not allowed.
StructField | The value type in Python of the data type of this field (for example, Int for a StructField with the data type IntegerType) | *StructField(name, dataType, [nullable])

Note: The default value of nullable is True.

__Overview of Structured API Execution__
Overview of execution steps
1. Write DataFrame/Dataset/SQL Code.
2. If valid code, Spark converts this to a Logical Plan.
3. Spark transforms this Logical Plan to a Physical Plan, checking for optimizations along the way.
4. Spark then executes this Physical Plan (RDD manipulations) on the cluster

### Basic Structured Operations
##### schema
- a `StructType` (Spark's complex types) made up of a number of fields;
- `StructFields` that have a name, type and boolean flag indicating whether that column can contain null values.
- optional metadata can be stored with that column.
- If the types in the data do match the shcema (at runtime), Spark throws an error.

```Python
from pyspark.sql.types import StructField, StructType, StringType, LongType

manualSchema = StructType([
  StructField("Home_country", StringType(), True),
  StructField("Away_country", StringType(), True),
  StructField("Score_diff", LongType(), Fasle), metadata={"hello":"world"}
  ])
df = spark.read.format("json").schema(manualSchema).load("/data/matches.json")
```

#### Columns and Expressions
- Selecting, manipulating and removing columns from a DataFrame are represented as _expressions_
- Columns are logical constructions that represent a va;ue computed on a per-record basis by means of an expressions.
- Can't manipulate individual columns outside the context of a DataFrame,
- Spark transformations must be used within a DataFrame to modify the contents of a column.

To construct and refer to columns:
```Python
from spark.sql.functions import col, column

# both are equivilent
col('aColumnName')
column('aColumnName')
```

To explicitly reference a column
`df.col("aColumnName")`

if `col()` is used, only transformations used on that column referenced.<br>
using expression, the `expr` function can parse transformations and column references from a string.<br>
`expr` can be used to refer to a plain column or a string manipulation of a column.
key points:
- Columns are just expressions
- Columns and transformations of those columns compile to the same logical plan as parsed expressions.

```Python
from pyspark.sql.functions import col, expr

expr("(((someCol + 5) * 200) - 6) < otherCol")
# equivalent
(((col("someCol") + 5) * 200) - 6) < col("otherCol")
```

SQL code and DataFrame code compile to same logical tree before execution, either can be used for exact same performance.

__accessing a DataFrames columns__ <br>
`df.columns`

#### Records and Rows
- each row in a DataFrame is a single record,
- each record is an object of type Row.

__to view first row__<br>
`df.first()`

Create rows by instantiating `Row` object with values that belong in each column.<br>
Note: the values have to be in the correct order as the schema of the DataFrame.
```Python
from pyspark.sql import Row

myRow = Row("Hello", None, 1, False)
```

#### DataFrame Transformations
##### Create  DataFrames
either from raw sources
```Python
df = spark.read.format("json").load("/data/flight-data/json/2015-summary.json")
df.createOrReplaceTempView("dfTable") # this allows manipulation via SQL
```
or manually create:
```Python
from pyspark.sql import Row
from pyspark.sql.types import StructField, StructType, StringType, LongType
myManualSchema = StructType([  
  StructField("some", StringType(), True),  
  StructField("col", StringType(), True),  
  StructField("names", LongType(), False)
])
myRow = Row("Hello", None, 1)
myDf = spark.createDataFrame([myRow], myManualSchema)
myDf.show(
```

##### select and selectExpr
Allows the equivalent of SQL queries to a DataFrame

easiest way is to use `select` method and pass column names as strings<br>
`df.select("DEST_COUNTRY_NAME").show(2`

to select multiple columns:<br>
`df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)`

Columns can be referred to in many ways - but they can't be used interchangeably
```Python
from pyspark.sql.functions import expr, col, column
df.select(    
  expr("DEST_COUNTRY_NAME"),    
  col("DEST_COUNTRY_NAME"),    
  column("DEST_COUNTRY_NAME"))\  
  .show(2)
```

`SelectExpr` is shorthand for `select` followed by `expr`.<br>
Using `selectExpr` you can build up complex expressions that create new DataFrames.<br>
an example that adds a new column `withinCountry` to the DataFrame:
```Python
df.selectExpr(
  "*", # all original columns
  "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")\
  .show(2)
```

##### Converting to Spark Types (Literals)
Literals are a translation from a programming language's literal value to one that Spark understands.<br>
Literals are expressions and can be used in the same way.
```Python
from pyspark.sql.functions import lit

df.select(expr("*"), lit(1).alias("One")).show(2)
```
is the same in SQL as:
```sql
SELECT *, 1 as ONE FROM dfTable LIMIT 2
```

##### Adding Columns
more formal way of adding column: `df.withColumn("numberOne", lit(1)).show(2)`<br>
`withColumn` takes two arguments: the column name and the expression that create the value for that given row in the DataFrame.<br>
`df.withColumn("withinCountry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME")).show(2)`


##### Renaming columns
we can rename a column with `withColumn` like: `df.withColumn("DEST_COUNTRY_NAME", expr("dest"))`<br>
but there is an alternative more explicit method `withColumnRenamed`: `df.withColumnRenamed("DEST_COUNTRY_NAME", "dest")`

##### Reserved Characters and Keywords
Use backtick (`) to escape column names with spaces or dashes.

##### Removing Columns
`df.drop("ORIGIN_COUNTRY_NAME")` <br>
to drop multiple columns: `df.drop("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME")`

##### Changing a Columns Type (Casting)
```Python
df.withColumn("count2", col("count").cast("long"))
```<br>
equivalent in sql as
```sql
SELECT *, CAST(count AS long) AS count2 FROM dfTable
```


##### Filtering Rows
```Python
# similar methods
df.filter(col("count") < 2).show(2)
df.where("count < 2").show(2)
```
```SQL
-- in SQL
SELECT * FROM dfTable WHERE count < 2 LIMIT 2
```
multiple filters can be in the same expression, but because Spark automatically does all filtering at the same time. So multiple `AND` filter can be chained sequentially.
```Python
df.where(col("count") < 3).where(col("ORIGIN_COUNTRY_NAME") != "USA").show(2)
```


##### Getting Unique Rows
A transformation that will only return unique rows.
```Python
df.select("ORIGIN_COUNTRY_NAME").distinct().count()
```


##### Random Samples
similar to Pandas sample method.
```Python
seed = 5
withReplacement = False
fraction = 0.5
df.sample(withReplacement, fraction, seed).count()
```


##### Random Splits
Splits the DataFrame into different DataFrames, by setting the weights of each (they should sum to 1.0 otherwise Spark will normalized so they do).<br>
because they random, a seed should be set.
```Python
dataFrames = df.randomSplit(Array([0.75, 0.25]),seed)
```


##### Concatenating and Appending Rows (Union)
To union 2 DataFrames, they have to have the same schema and same number of columns.
```Python
from pyspark.sql import Row

# create a new DataFrame
schema = df.schema
newRows = [
     Row("New Country", "Other Country", 5L),  
     Row("New Country 2", "Other Country 3", 1L)
]
parallelizedRows = spark.sparkContext.parallelize(newRows)
newDF = spark.createDataFrame(parallelizedRows, schema)

df.union(newDF)\
    .where("count = 1")\
    .where(col("ORIGIN_COUNTRY_NAME") != "United States")\
    .show()
```
The new DataFrame reference has to be used to refer to DataFrame with the appended rows. A common way, is to make the DataFrame into a view or register it as a table so it can be reference more dynamically in code.


##### Sorting Rows
Two equivalent operations `sort` and `orderBy`. Both take column expressions and strings as well as multiple columns. The default is ascending.
```Python
df.sort("count").show(5)
df.orderBy("count", "DEST_COUNTRY_NAME").show()
df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)
```
to explicitly specify sort direction use `asc` and `desc`
```Python
from pyspark.sql.functions import asc, desc

df.orderBy(expr("count desc")).show(2)
df.orderBy(col("count").desc(), col("DEST_COUNTRY_NAME").asc()).show(2)
```
to specify where you want nulls to appear when ordered use: `asc_nulls_first`, `desc_nulls_first`, `asc_nulls_last` or `desc_nulls_last`<br>
For optimization purpose, it be advisable to sort within each partition (`sortWithinPartitions`) before another set of transformation.


##### Limit
restrict number of rows extracted
```Python
df.limit(5).show()`
df.orderBy(expr("count desc")).limit(10).show()
```


##### Repartition and Coalesce
An important optimization opportunity is to partition dat according to some frequently filtered columns, which control the physical layout of data across the cluster including the partitioning scheme and the number of partitions.

Note: Repartition will incur full shuffle of the data. Therefore repartition is commonly done when the future number of partitions are more than the current number or when partitioning by a set of columns.
```Python
df.rdd.getNumPartitions() # returns number of partitions

df.repartition(5)
```

if filtering by a certain column often, it might be worth repartitioning based on the column. The number of partitions can be optionally specified
```Python
df.repartition(col("DEST_COUNTRY_NAME"))
df.repartition(5, col("DEST_COUNTRY_NAME"))
```

`coalesce` will not incur a full shuffle, and will combine partitions.
```Python
# repartition into 5, then used combine to 2 using coalesce
df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)
```


##### Collecting Rows to the Driver
- `collect()` gets all the data from the entire DataFrame
- `take` selects the first _N_ rows
- `show` prints out a number of rows nicely


### Working with different types of data
Where to look for APIs
##### Converting to SparkTypes
`Lit` converts another languages type to Spark representation of it
```Python
from pyspark.sql.functions import Lit
df.select(Lit(5), Lit("five"), Lit(5.0))
```
##### Working with Booleans
```from pyspark.sql.functions import col
df.where(col("InvoiceNo") != 536365)\
  .select("InvoiceNo", "Description")\
  .show(5, False)
```
Can also be expressed as an expression in a string:
`df.where("InvoiceNo <> 536365").show(5, False)`<br>
Boolean expression with multiple parts can be specified using `and` or `or`.
It's best to always chain together `and` filters as a sequential filter. As spark will
flatten all the filters into one, and perform the filter at the same time (creating the `and` statement for us).<br>
`or` statements need to be specified in the same statement.
```Python
from pySpark.sql.functions import instr # search chars 'in str', returns 0 if not present
priceFilter = col("UnitPrice") >600
descripFilter = instr(df.Description, "POSTAGE") >= 1
df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show()
```
To filter with a boolean column:
```Python
DOTCodeFilter = col("StockCode") == "DOT"
priceFilter = col("UnitPrice") > 600
descripFilter = instr(col("Description"), "POSTAGE") >= 1
df.withColumn("isExpensive", DOTCodeFilter & (priceFilter | descripFilter))\
  .where("isExpensive")\
  .select("unitPrice", "isExpensive").show(5)
```
the equivalent in SQL:
```sql
SELECT UnitPrice, (StockCode == "DOT" AND
       (UnitPrice > 600 OR instr(Description, "POSTAGE") >= 1)) as isExpensive
FROM dfTable
WHERE (StockCode = "DOT" AND
      (UnitPrice > 600 OR instr(Description, "Postage") >= 1))
```
The filter need not be an expression and we can use a column name easily.<br>
It is easier to express filters as SQL statements that using DataFrame interface.
```Python
from pyspark.sql.functions import expr
df.withColumn("isExpensive", expr("NOT UnitPrice <= 250"))\
  .where("isExpensive")\
  .select("Description", "UnitPrice").show(5)
```


##### Working with Numbers
`from pyspark.sql.functions'
- 'pow` for `pow(lit(2),3)` 2^3
- `round` for rounding and `bround` to round down
- 'corr' for Pearson Correlation
-  `count`, `mean`, `stddev_pop`, `min`, `max` for summary statistics or `df.describe().show()`
- `monotonically_increasing_id` generates an increasing unique id starting at 0
<br>
There are statistical functions available in the StatFunction package<br>
```python
colName = "UnitPrice"
quantileProbs = [0.5]
relError = 0.05
df.stat.approxQuantile("UnitPrice", quantileProbs, relError) # 2.51
```


##### Working with Strings
- `initcap` capitalizes every word seperated by a space.
- `lower` and `upper` to change cases of the letters
- removing white space with:
```Python
from pyspark.sql.functions import lit, ltrim, rtrim, rpad, lpad, trim
df.select(    
     ltrim(lit("    HELLO    ")).alias("ltrim"),    
     rtrim(lit("    HELLO    ")).alias("rtrim"),    
     trim(lit("    HELLO    ")).alias("trim"),    
     lpad(lit("HELLO"), 3, " ").alias("lp"),    
     rpad(lit("HELLO"), 10, " ").alias("rp")).show(2)
```
* note if `lpad` or `rpad` takes a number less than the length of the string,
it will always remove values from the right side of the string.

###### Regular Expressions
Spark uses the complete power of Java Regular Expressions.<br>
key functions are `regexp_extract` and `regexp_replace`


##### Working with Dates and Timestamps
- Spark timestamp is till the seconds
- any smaller meaurement in time is best to try to use `longType`

```python
from pyspark.sql.functions import current_date, current_timestamp
dateDF = spark.range(10)\
    .withColumn("today", current_date())\
    .withColumn("now", current_timestamp())
dateDF.createPrReplaceTempView("dateTable")
```
To add/subtract days:
```Python
from pyspark.sql.functions import date_add, date_sub
dateDF.select(date_sub(col("today"), 5), date_add(col("today"), 3)).show(1)
```
Difference between two dates:
```Python
from pyspark.sql.functions import datediff, months_between, to_date
dateDF.withColumn("week_ago", date_sub(col("today"), 7))\
  .select(datediff(col("week_ago"), col("today"))).show(1)

dateDf.select(
    to_date(lit("2016-01-01")).alias("start"),    
    to_date(lit("2017-05-22")).alias("end"))\
  .select(months_between(col("start"), col("end"))).show(1))
)
```
`to_date` converts a string to a date, with optional specified format.
__note:__ Spark will return `null` if it can't parse the date - without throwing error!
The date format should be according the Java `SimpleDateFormat` standard of `yyyy-MM-dd`

convert to date or datetime (latter requires format):
```Python
from pyspark.sql.functions import to_date, to_timestamp
dateFormat = "yyyy-dd-MM"
cleanDateDF = spark.range(1).select(    
    to_date(lit("2017-12-11"), dateFormat).alias("date"),    
    to_date(lit("2017-20-12"), dateFormat).alias("date2"))
cleanDateDF.createOrReplaceTempView("dateTable2")

cleanDateDF.select(to_timestamp(col("date"), dateFormat)).show()
```


##### Working with Nulls in data
- `Coalesce` returns the first non-null value
- `ifnull` returns second value if 1st is null, defaults to first
- `nullif` returns null if two values are equal, otherwise returns the second value.
- `nvl` returns 2nd value if 1st is null, defaults to the first value.
- `nvl2` returns the 2nd value if the 1st is not null, otherwise will return the last specified value.
- drop `df.na.drop("all")` will drop row if all values are null or NaN, the default is "any". can be applied to a subset of columns
- fill: using a Scala Map we can fill in values for columns
  ```Python
  fill_cols_vals = {"StockCode": 5, "Description" : "No Value"}
  df.na.fill(fill_cols_vals)
  ```
- replace `df.na.replace([""], ["UNKNOWN"], "Description")` the only requirement to replacing values is that they have to be replaced with the same type.


##### Ordering
using  `asc_nulls_first`, `desc_nulls_first`, `asc_nulls_last`, or `desc_nulls_last` to dictate where you want nulls to appear in the DataFrame.


##### Working with Complex Types
- - [ ] Structs
- - [ ] Arrays
- - [ ] split
- - [ ] Array Length
- - [ ] array_contains
- - [ ] explode
- - [ ] Maps
##### Working with JSON
##### User-Defined Functions (UDF)
- functions written by user to preform specific transformations.
- can be written in any language
- - but performance considerations
- best to write functions in Scala
- once UDF is registered in Spark, can be used in SparkSQL as well
- optional, but best pratice to define return type when registering udf

```Scala
// in Scala
val udfExampleDF = spark.range(5).toDF("num")
def power3(number:Double):Double = number * number * number
power3(2.0)

//register udf in Spark
import org.apache.spark.sql.functions.udf
val power3udf = udf(power3(_:Double):Double)

//can be used like any other spark function
udfExampleDF.select(power3udf(col("num"))).show()

// power3udf can be used only as DataFrame function.
// Registering function as SparkSQL function makes it usable within SQL as well as across languages

spark.udf.reister("power3", power3(_:Double):Double)
udfExampleDF.selectExpr("power3(num)").show()
```


### Aggregations
#### Aggregations Functions
##### count
- if used as an action, eagerly evaluated `df.count()`, or
- transformation, specifying a specific column, or all
##### countDistinct
- count the number of unique groups
##### approx_count_distict
`pprox_count_distinct(<column>, <err>)`
- used on large datasets where the exact distinct count is not important, and  an approximate will do
- performance gain
- `<err>`: maximum estimation error parameter
##### first and last
- based on the rows of a dataframe
##### min and max
- extraxt minimum and maximum values.
##### sum
- add all the values
##### sumDisctint
- sum a distinct set of values.
##### avg
```python
from pyspark.sql.functions import sum, count, avg, expr
df.select(
    count("Quantity").alias("total_transactions"),    sum("Quantity").alias("total_purchases"),    avg("Quantity").alias("avg_purchases"),    expr("mean(Quantity)").alias("mean_purchases"))\
  .selectExpr(
      "total_purchases/total_transactions",    "avg_purchases",    "mean_purchases").show()
```
##### Variance and Standard Deviation
- spark has both sample and population variance and standard deviation
```Python
from pyspark.sql.functions import var_pop, stddev_pop
from pyspark.sql.functions import var_samp, stddev_samp
df.select(var_pop("Quantity"), var_samp("Quantity"),
          stddev_pop("Quantity"), stddev_samp("Quantity")).show()
```
##### skewness and kurtosis
- measurements of extreme points in the data
- - skewness: asymetry of the values in data around the mean
- - kurtosis: measure of the tail of the data
##### Covariance and Correlation
- covariance has a population and sample formula
```Python
from pyspark.sql.functions import corr, covar_pop, covar_samp df.select(covar_pop("InvoiceNo", "Quantity"), covar_samp("InvoiceNo", "Quantity"),
          corr("InvoiceNo", "Quantity")).show()
```
##### Aggregating to Complex Types
In spark you can also perform aggregations on complex types.
For example, we can collect a list of values present in a given column or only the unique values by collexting to a set.
```Python
from pyspark.sql.functions import collect_set, collect_list
df.agg(collect_set("Country"), collect_list("Country")).show()
```
#### Grouping
Grouping happens in two phases; first `RelationalGroupedDataset`, then second step returns a `DataFrame`<br>
`df.groupBy("InvoiceNo", "CustomerId").count().show()`
##### Grouping with Expressions
Rather than specifying in `Select` statement, it's easier to specify within `agg`.<br>
This makes possible to pass in arbitrary expressions that need some aggregation specified. `alias` a column after transforming it for use in the data flow
```Python
from pyspark.sql.functions import count
df.groupBy("InvoiceNo").agg(
     count("Quantity").alias("quan"),
     expr("count(Quantity)")).show()
)
```
##### Grouping with Maps
Sometime easier to specify tranformations as a series of `maps`; key is the columns, and value is the aggregation function (as a string). You can reuse multiple column names if specified inline.
```Python
df.groupBy("InvoiceNo").agg(expr("avg(Quantity)"), expr("stddev_pop(Quantity)"))\
.show()
```
#### Window Functions
first create a window specification, the frame specification (`rowsBetween`) states which rows to be included in the frame based on its reference to the current row.<br>
In this example, all previous rows are included.
```Python
from pyspark.sql.window import Window
from pyspark.sql.funtions import desc
windowSpec = Window\
              .partitionBy("CustomerId", "date")\
              .orderBy(desc("Quantity"))\
              .rowsBetween(Window.unboundedPreceding, Window.current_row)
```
We can use an aggregation function passing in column name or expression, and indicate the window specification that defines to which frames of the data the function applies to.
```python
from pyspark.sql.functions import max
maxPurchaseQuantity = max(col("Quantity")).over(windowSpec)
```
The result is a column or expression, which can be used in a DataFrame select statement.<br>
To calculate maximum quantity purchased for every customer, `dense_rank` can be used to avoid gaps in the ranking sequence when there are tied values (or duplicate rows).
```Python
from pyspark.sql.functions import dense_rank, rank
purchaseDenseRank = dense_rank().over(windowSpec)
purchaseRank = rank().over(windowSpec)
```
A select can be performed to view the calculated window values.
```Python
from pyspark.sql.functions import col

dfWithDate.where("Customer IS NOT NULL").orderBy("CustomerId")\
  .select(
    col("CustomerId"),
    col("date"),
    col("Quantity"),
    purchaseRank.alias("quantityRank"),
    purchaseDenseRank.alias("quantityDenseRank"),
    maxPurchaseQuantity.alias("maxPurchaseQuantity")
  ).show()
```

which is the equivalent in SQL to:
```sql
SELECT CustomerId, date, Quantity,
  rank(Quantity) OVER (PARTITION BY CustomerId, date
                       ORDER BY Quantity DESC NULLS LAST
                        ROWS BETWEEN
                          UNBOUNDED PRECEDING AND
                          CURRENT ROW) as rank,
  dense_rank(Quantity) OVER (PARTITION BY CustomerId, date
                            ORDER BY Quantity DESC NULLS LAST
                            ROWS BETWEEN
                              UNBOUNDED PRECEDING AND
                              CURRENT ROW) as dRank,
  max(Quantity) OVER (PARTITION BY CustomerId, date
                      ORDER BY Quantity DESC NULLS LAST
                      ROWS BETWEEN
                        UNBOUNDED PRECEDING AND
                        CURRENT ROW) as maxPurchase
FROM dfWithDate
WHERE CustomerId IS NOT NULL ORDER BY CustomerId
```


#### Grouping Sets
- a low-level tool for combining sets of aggregations together.
- ability to create arbitrary aggregation in their group-by statements.
The GROUPING SETS operator is only available in SQL. To perform the same in DataFrames, you use the rollup and cube operators—which allow us to get the same results

##### Rollups
A rollup is a multidimensional aggregation that performs a variety of group-by style calculations.<br>
example: Rollup that looks across time(`date`) and space(`Country`) and creates a DataFrame that includes the grand total over all the dates, the grand total for each date, and the subtotal for each country on each date in the DataFrame.
```Python
rolledUpDf = dfNoNull.rollup("Date", "Country").agg(sum("Quantity"))\
  .selectExpr("Date", "Country", "`sum(Quantity)` as total_quantity")\
  .orderBy("Date")
rolledUpDf.show()
```
null values is where you’ll find the grand totals. A null in both rollup columns specifies the grand total across both of those columns.

##### Cube
A cube takes a rollup a level deeper.  Rather than treating elements hierarchically, a cube does the same thing across all dimensions.
```Python
from pyspark.sql.functions import sum

dfNoNull.cube("Date", "Country").agg(sum(col("Quantity")))\
    .select("Date", "Country", "sum(Quantity)").orderBy("Date").show()
```
This is a quick and easily accessible summary of nearly all of the information in our table, and it’s a great way to create a quick summary table that others can use later on.

##### Grouping Metadata

##### Pivot
Converts a row into a column.
```Python
pivoted = dfWithDate.groupBy("date").pivot("Country").sum()
```
This DataFrame will vabe a column for every combination of country, numeriv variable and a date column.<br>
It can be useful, if you have low enough cardinality in a certain column to transform it into columns so that users can see the schema and immediately know what to query for.

#### User-Defined Aggregation Functions
UDAFs are currently available only in Scala or Java


### Joins
#### Join Expressions
The most common join expression, an `equi-join`, compares whether the specified keys in your left and right datasets are equal. If they are equal, Spark will combine the left and right datasets
#### Join Types
- join expression determines whether two rows *should* join
- join type determines *what* should be the result.

different types of joins in Spark:
- `"inner"` Inner joins (keep rows with keys that exist in the left and right datasets), default join
- `"outer"` Outer joins (keep rows with keys in either the left or right datasets)
- `"left_outer"` Left outer joins (keep rows with keys in the left dataset)
- `"right_outer"` Right outer joins (keep rows with keys in the right dataset)
- `"left_semi"` Left semi joins (keep the rows in the left, and only the left, dataset where the key appears in the right dataset)
- `"left_anti"` Left anti joins (keep the rows in the left, and only the left, dataset where they do not appear in the right dataset)
- Natural joins (perform a join by implicitly matching the columns between the two datasets with the same names)
- `"cross"` Cross (or Cartesian) joins (match every row in the left dataset with every row in the right dataset)
- - If you truly intend to have a cross-join, you can call that out explicitly: `person.crossJoin(graduateProgram).show()`

```Python
joinExpression = person["graduate_program"] == graduateProgram['id']
joinType = "inner"

person.join(graduateProgram, joinExpression, joinType),show()
```

#### Challenges when using Joins
##### Joins on Complex Types
Any expression is a valid join expression if it returns a Boolean.
```Python
from pyspark.sql.functions import expr

person.withColumnRenamed("id", "personId")\
  .join(sparkStatus, expr("array_contains(spark_status, id)")).show()
```
##### Handling Duplicate Column Names
###### approach1: different join expression
easiest fix is to change join expression from a Boolean to a string or sequence. This automatically removes one of the columns.
###### approach2: dropping the column after join
Drop the offending column after the join. When referring to the column we need to refer to original source of the DataFrame.
###### approach3: renaming column before the join
Renaming one of the columns avoids the issue completely
#### How Spark performs Joins
Spark approaches cluster communication in two different ways during joins. It either incurs a shuffle join, which results in an all-to-all communication or a broadcast join<br>
**shuffle-join**<br>
- every node talks to every node and share data accordingly.
- joins are expensive and can cause network congestion

**broadcast join**<br>
- if table can fit in memmory of single worker node
- replicate small DataFrame onto every worker node in cluster.
- initial large communication, then no further comunication between nodes.
- CPU becomes the biggest bottleneck
##### Communications strategies
###### Big-table-to-big-table
- shuffle-join
###### Big-table-to-small-table
- broadcast join
###### Little table–to–little table
best to let Spark decide


### Data Sources
#### Structure of Data Sources API
##### Read API Structure
##### Basics of Reading Data
##### Write API Structure
##### Basics of Writing Data
#### CSV Files
##### CSV Options
##### Reading csv
##### Writing csv
#### JSON Files
##### json Options
##### Reading json
##### Writing json
#### Parquet Files
##### Reading Parquet
##### Writing Parquet
#### ORC Files
##### Reading Orc
##### Writing Orc
#### SQL Databases
##### Reading from SQL databases
##### Query Pushdown
##### Writing to SQL databases
#### Text Files
##### Reading Text
##### Writing Text
#### Advanced I/O Concepts
##### Splitting File Types and Compression
##### Reading data in Parallel
##### Writing data in Parallel
##### Writing Complex Types
##### Managing File Size


### Spark SQL
#### Big Data and SQL: Apache Hive
#### Big Data and SQL: Spark SQL
##### Spark’s Relationship to Hive
- can cpnnect to Hive metastore and access table metadata to reduce file listing when accessing information.
#### How to Run Spark SQL Queries
to connect to Hive metastore:
- set Metastore version (default 1.2.1) `spark.sql.hive.metastore.version`
- set `spark.sql.hive.meatstore.jars` if changing the way `HiveMetastoreClient` is intialized.
set shared prefixes `spark.sql.hive.metastore.sharedPrefixes ` in order to communicate with databases that store the Hive metastore.
##### Spark SQL CLI
- make basic Spark SQL queries in local mode from command line.
- can't communicate with the Thrift JDBC server.
- start Spark SQL CLI, run `./bin/spark-sql` in the Spark directory
##### Spark’s Programmatic SQL Interface
- execute SQL using `sql` method on the `SparkSession` object.
- returns a DataFrame.
- executed lazily
- multiline queries can be passed using multiline string
```python
spark.sql("""SELECT user_id, department, first_name FROM professors
  WHERE department in
  (SELECT name FROM department WHERE created_date >= "2018-09-02")""")
```
- can completely interoperate between SQL and DataFrames. ie create DataFrame, manipulate with SQL, and then manipulate again as a DataFrame.
```Python
spark.read.json("/data/flight-data/json/2015-summary.json")\
  .createOrReplaceTempView("some_sql_view") # DF => SQL
spark.sql("""
SELECT DEST_COUNTRY_NAME, sum(count)
FROM some_sql_view
GROUP BY DEST_COUNTRY_NAME """)\
  .where("DEST_COUNTRY_NAME like 'S%'").where("`sum(count)` > 10")\
  .count() # SQL => DF
```


##### SparkSQL Thrift JDBC/ODBC Server
- remote program connects to Spark driver to execute Spark SQL queries.
- common use to connect business intelligence software like Tableau to Spark.
start JDBC/ODBC server run `./sbin/start-thriftserver.sh` in Spark directory
- scripts accepts all `bin/spark-submit` command line options.
- by default listens on localhost:10000.
#### Catalog
abstraction for storage of metadata about data stored in tables, and about databases, tables, functions and views.<br>
#### Tables
- first need to define tables, logically equivalent ot DataFrames; in that they are a structure of data which you run commands.
- core difference between tables and DataFrames:
- - define DataFrames in the scope of a programming language
- - define tables within a database. (will belong to default database)
- tables always contain data; no temporary tables, only views that doesn't contain data.
- - if your drop a table, you risk losing data.
##### Spark-Managed Tables
- tables store data within the table, as well as data about the tables (metadata).
- when tables are defined from disk; unmanaged table.
- when use `saveAsTAble` on a DataFrame; managed table which Spark will track all of the relevant info.
##### Creating Tables
- no need to define a table and then load data into it. Create one on the fly
- can specify sophisticated options when read in a file.

```Python
spark.sql("""
  CREATE TABLE flights(
    DEST_COUNTRY_NAME STRING, ORIGIN_COUNTRY_NAME STRING, count LONG)
  USING JSON OPTIONS (path "/data/flight-data/json/2015-summary.json")
  )"""
```
if `USING` is not specified, Spark will default to Hive SerDe configuration that can impact performance.
- comments can be added to certain columns in a table which can aid developers in understanding the data.

```Python
spark.sql("""
  CREATE TABLE flights_csv (
    DEST_COUNTRY_NAME STRING,
    ORIGIN_COUNTRY_NAME STRING COMMENT "remember, US will be most prevalent",
    count LONG)
  USING csv OPTIONS(header true, path "/data/flight-data/json/2015-summary.json")
  )"""
```
- create table from a query: `CREATE TABLE flights_from_select USING parquet AS SELECT * FROM flights`
- you can control the layout of the data by writing out a partitioned dataset
```Python
spark.sql("""
  CREATE TABLE partitioned_flights USING parquet PARTITIONED BY (DEST_COUNTRY_NAME)
  AS SELECT DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME, count FROM flights LIMIT 5
""")
```
##### Creating External Tables
##### Inserting into Tables
##### Describing Table Metadata
- can view comments
`spark.sql("DESCRIBE TABLE flights_csv")`
- view patitioning sheme on partitioned tables
`SHOW PARTITIONS partitioned_flights`
##### Refreshing Table Metadata
- `REFRESH TABLE` refreshes all cached entries associated with the table.
- `REPAIR TABLE` refreshes the partitions maintained in the catalog for that table.
- - focuses on collecting new partition information.
##### Dropping Tables
- can't delete table, can only drop them.
- dropping a managed table will remove both the data and the table definition.
- dropping an unmanaged table, no data will be removed.
`DROP TABLE <name>;` or avoid error if table doesn't exist `DROP TABLE IF EXISTS <name>;`
##### Caching Tables
`CACHE TABLE <name>` and `UNCACHE TABLE <name>`
#### Views
- specifies a set of transformations on top of an existing table.
- like saved query plans, convenient for organising or reusing query logic.
- can be global, set to a database or per session.
##### Creating Views
- displayed as tables
- performs transformations on source data at query time.
create temporary view, available only during current session
```python
spark.sql("""
  CREATE TEMP VIEW temp__view_name AS
    SELECT * FROM flights WHERE DEST_COUNTRY_NAME = "US"
""")
```
can overwrite if one already exists
```python
spark.sql("""
CREATE OR REPLACE GLOBAL VIEW temp_name AS
  SELECT * FROM flights WHERE DEST_COUNTRY_NAME = "US"
""")
```
Global temp views are resolved regardless of database and viewable across entire Spark application, but removed after the session.
##### Dropping Views
- dropping a view removes only the definition itself, not the underlying data
`DROP VIEW IF EXISTS temp_view_name`
#### Databases
- tool for organising tables
- any SQL statement (including DataFrame commands) execute within the context of a database.
- if you change databse, any user-defined tables will remain in the previous database and will need to be queried differently.
- `SHOW DATABASES` see all databases
##### Creating Databases
`CREATE DATABASE some_db`
##### Setting the Database
- set a databse to perform certain query: `USE some_db`
- afterwards, all queries will resolve table names to this database.
- query different database by using correct prefix: `SELECT * FROM default.flights`
- see current database using: `SELECT current_database()`
##### Dropping Databases
`DROP DATBASE IF EXISTS some_db;`
#### Select Statements
follows ANSI SQL
##### case…when…then Statements
like programmatic `if` statements
```python
spark.sql("""
  SELECT
    CASE WHEN DEST_COUNTRY_NAME = "UNITED STATES" THEN 1
         WHEN DEST_COUNTRY_NAME = "EGYPT" THEN 0
         ELSE -1
    END
  FROM partitioned_flights
""")
```
#### Advanced Topics
##### Complex Types
- powerful that doesn't exist in standard SQL
- structs, lists and maps.
###### Structs
- more akin to maps
- provide a way of creating or querying nested data in Spark
- create one by wrapping set of columns (or expressions) in parenthesis
```sql
CREATE VIEW IF NOT EXISTS nested_data AS
  SELECT (DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME) as country, count
  FROM flights
```
- query individual columns within a struct using dot syntax
`SELECT country.DEST_COUNTRY_NAME, count from nested_data`
- select all (sub)columns from struct
`SELECT country.*, count FROM nested_data`
###### Lists
- `collect_list` creates a list of values.
- `collect_set` creates array without duplicate values.
- These are both aggregation functions and therefore can only be specified in aggregations.
```spark.sql("""
    SELECT DEST_COUNTRY_NAME as new_name, collect_list(count) as flight_counts,
      collect_set(ORIGIN_COUNTRY_NAME) as origin_set
    FROM flights GROUP BY DEST_COUNTRY_NAME
""")
```
- manually create array within column
`SELECT DEST_COUNTRY_NAME`, ARRAY(1,2,3) FROM flights
- query lists by position (zero-indexed)
`SELECT DEST_COUNTRY_NAME as new_name, collect_list(count)[0] FROM flights GROUP BY DEST_COUNTRY_NAME`
##### Functions
- Spark SQL provides variety of sophisticated functions
- `SHOW FUNCTIONS` list of functions in Spark SQL
- `SHOW SYSTEM FUNCTIONS` see builtin functions
- `SHOW USER FUNCTIONS` see user-defined functions
- filter `SHOW` commands
- - list functions that start with 'S' `SHOW FUNCTIONS "s*"`
##### Subqueries
###### Uncorrelated predicate subqueries
- do not include information from the outer scope of the query. a query you can run on its own
###### Correlated predicate subqueries
- use information from the outer scope in the inner query
###### Uncorrelated scalar queries
used to bring in supplemental information not had previously.
#### Miscellaneous Features
##### Configurations
##### Setting Configuration Values in SQL
`SET spark.sql.shuffle.partitions=20`
