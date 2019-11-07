
#### Chapter 1 - 4:
- [x] Overview and light reading 6/11/2019

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
- - [x] Changing Column's Type (cast) 7/11/2019
- - [ ] Filtering Rows
- - [ ] Getting Unique Rows
- - [ ] Random Samples
- - [ ] Random Splits
- - [ ] Concatenating and Appending Rows (Union)
- - [ ] Sorting Rows
- - [ ]  Limit
- - [ ] Repartition and Coalesce
- - [ ] Collecting Rows to the Driver

### Working with different types of data
- [ ] Where to look for APIs
- [ ] Converting to SparkTypes
- [ ] Working with Booleans
- [ ] Working with Numbers
- [ ] Working with Strings
- - [ ] Regular Expressions
- [ ] Working with Dates and Timestamps
- [ ] Working with Nulls in data
- - [ ] Coalesce
- - [ ] ifnull, nullifm nvl, and nvl2
- - [ ] drop
- - [ ] fill
- - [ ] replace
- [ ] Ordering
- [ ] Working with Complex Types
- - [ ] Structs
- - [ ] Arrays
- - [ ] split
- - [ ] Array Length
- - [ ] array_contains
- - [ ] explode
- - [ ] Maps
- [ ] Working with JSON
- [ ] User-Defined Functions

### Aggregations
- [ ] Aggregations Functions
- - [ ] count
- - [ ] countDistinct
- - [ ] approx_count_distict
- - [ ] first and last
- - [ ] min and max
- - [ ] sum
- - [ ] sumDisctint
- - [ ] avg
- - [ ] Variance and Standard Deviation
- - [ ] skewness and kurtosis
- - [ ] Covariance and Correlation
- - [ ] Aggregating to Complex Types
- [ ] Grouping
- - [ ] Grouping with Expressions
- - [ ] Grouping with Maps
- [ ] Window Functions
- [ ] Grouping Sets
- - [ ] Rollups
- - [ ] Cube
- - [ ] Grouping Metadata
- - [ ] Pivot
- [ ] User-Defined Aggregation Functions

### Joins
- [ ] Join Expressions
- [ ] Join Types
- [ ] Inner Joins
- [ ] Outer Joins
- [ ] Left Outer Joins
- [ ] Right Outer Joins
- [ ] Left Semi Joins
- [ ] Left Anti Joins
- [ ] Natural Joins
- [ ] Cross (Cartesian) Joins
- [ ] Challenges when using Joins
- - [ ] Joins on Complex Types
- - [ ] Handling Duplicate Column Names
- [ ] How Spark performs Joins
- - [ ] Communications strategies

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
- [ ] Big Data and SQL: Apache Hive
- [ ] Big Data and SQL: Spark SQL
- - [ ] Spark’s Relationship to Hive
- [ ] How to Run Spark SQL Queries
- - [ ] Spark SQL CLI
- - [ ] Spark’s Programmatic SQL Interface
- - [ ] SparkSQL Thrift JDBC/ODBC Server
- [ ] Catalog
- [ ] Tables
- - [ ] Spark-Managed Tables
- - [ ] Creating Tables
- - [ ] Creating External Tables
- - [ ] Inserting into Tables
- - [ ] Describing Table Metadata
- - [ ] Refreshing Table Metadata
- - [ ] Dropping Tables
- - [ ] Caching Tables
- [ ] Views
- - [ ] Creating Views
- - [ ] Dropping Views
- [ ] Databases
- - [ ] Creating Databases
- - [ ] Setting the Database
- - [ ] Dropping Databases
- [ ] Select Statements
- - [ ] case…when…then Statements
- [ ] Advanced Topics
- - [ ] Complex Types
- - [ ] Functions
- - [ ] Subqueries
- [ ] Miscellaneous Features
- - [ ] Configurations
- - [ ] Setting Configuration Values in SQL

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

*Note: The default value of nullable is True.

__Overview of Structured API Execution__
Overview of execution steps<br>
1. Write DataFrame/Dataset/SQL Code.
2. If valid code, Spark converts this to a Logical Plan.
3. Spark transforms this Logical Plan to a Physical Plan, checking for optimizations along the way.
4. Spark then executes this Physical Plan (RDD manipulations) on the cluster

### Basic Structured Operations
##### schema
- a `StructType` (Spark's complex types) made up of a number of fields;
- `StructFields` that have a name, type and boolean flag indicating whether that column can contain null values.
- optional metadata can be stored with that column.
- If the typesin the data do match the shema (at runtime), Spark throws an error.
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
```SQL
SELECT *, CAST(count AS long) AS count2 FROM dfTable
```

##### Filtering Rows
##### Getting Unique Rows
##### Random Samples
##### Random Splits
##### Concatenating and Appending Rows
##### Sorting Rows
##### Limit
##### Repartition and Coalesce
##### Collecting Rows to the Driver
