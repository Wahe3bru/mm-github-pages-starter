---
title: MongoDB notes
last_modified_at: 2019-10-11T15:17:02-05:00
categories:
  - blog
tags:
  - python
  - MongoDB
  - notes
classes: wide
header:
  overlay_image: https://source.unsplash.com/collection/8375052/1024x720
excerpt:
---

MongoDB |JSON| Python
-|-|-
Databases |Objects| Dictionaries
↳Collections |Arrays| Lists
↳↳Documents |Objects| Dictionaries
↳↳↳Subdocuments |Objects| Dictionaries
↳↳↳ Values|Value types|Value types + datetime , regex...

## The Noble Prize API Data
``` python
import requests
from pymongo import MongoClient
# Client connects to "localhost" by default
client = MongoClient()
# Create local "nobel" database on the fly
db = client["nobel"]
for collection_name in ["prizes", "laureates"]:
# collect the data from the API
response = requests.get(
"http://api.nobelprize.org/v1/{}.json".\
format(collection_name[:-1] ))
# convert the data to json
documents = response.json()[collection_name]
# Create collections on the fly
db[collection_name].insert_many(documents)
```

Accessing databases and Collections
- using `[]`
```Python
# client is a dictionary of databases
db = client["nobel"]
# database is a dictionary of collections
prizes_collection = db["prizes"]
```
- using `.`
```Python
# databases are attributes of a client
db = client.nobel
# collections are attributes of databases
prizes_collection = db["prizes"]
```

##### methods
__aggregations__
`db.laureates.count_documents(filter)`

`db.laureates.distinct(gender,[filter])`
- is efficient if their is a collection index on the field
- has optional filter

__query__
`.find()`
`.find_one()`

#### filter
filters are a document with key values to match
```Python
db.laureates.count_documents({'gender': 'male'})
# or combine multiple
filter = {'gender':'male',
    'diedCountry': 'Germany'}
db.laureates.count_documents(filter)
```

##### Query operators
for non exact filtering, query operators are used
- value in  a range `$in:<list>`
- not equal `$ne: <value>`
- comparisons
- - >:`$gt`, >=: `$gte`
- - <: `$lt`, <=: `$lte`
- logical
- - `$and`
- - `$not`
- - `$or`, `$nor`
```Python
db.inventory.find({"status": {"$in": ["OK", "Fault"]}})
```
#### dot notation to reach into subfields
can specify fields deeper than root directory, can be used in query methods and aggregations

Distinct values
Distinct values given filters
Filter Arrays using distinct values

Projection
Sorting
Indexes
Limits

Aggregation
Aggregation operators and Grouping
Zoom into Array Fields
$addFields to aid analysis 

----
some  considerations
__To embed or not to embed?__
- is the embedded data wanted _80% of the time?_
- how often do you want the embedded data _without the containing document?_
- is the embedded data a _bounded set?_
- is that bound _small?_
- how _varied_ are your queries?
- are you working with intergrationdb or applicationdb
