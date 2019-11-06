
#### Chapter 1 - 4:
- [x] Overview and light reading

## Section II - Structure APIs
### Structured API Overview
- [ ] DataFrames and Datasets
- [ ] Schemas
- [ ] Overview of Structured Spark Types
- - [ ] DataFrames vs Datasets
- - [ ] Columns
- - [ ] Rows
- - [ ] SparkTypes
- Overview of Structured API Execution
- - [ ] Logical Planning
- - [ ]  Physical Planning
- - [ ] Execution

### Basic Structured Operations
- [ ] Schemas
- [ ]  Columns and Expressions
- - [ ] Columns
- - [ ] Expressions
- [ ] Records and Rows
- - [ ] Creating Rows
- [ ] DataFrame transformations
- - [ ] Creating DataFrames
- - [ ] select and selectExpr
- - [ ] Converting to Spark Types (Literals)
- - [ ] Adding Columns
- - [ ] Renaming Columns
- - [ ] Reserved Characters and Keywords
- - [ ] Case Sensitivity
- - [ ] Removing Columns
- - [ ] Changing Column's Type (cast)
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
