
## Downloading data
https://csvkit.readthedocs.io/
### Downloading data using curl
syntax: curl [option flags] [URL]<br>
URL is required. `curl` also supports `HTTP`, `HTTPS`, `FTP` and `SFTP`

optional flags:
All flags occur before the url and order doesn't matter

- `-O`: save file with its original name
- `-o`: save file as (with name provided)
- `L`: Redirects HTTP URL if error code 300 occurs
- `-C`: Resumes previous file transfer if it times out before completion

**Downloading multiple files**<br>
- `url -O http://www.website.com/datafile*.txt`: dl all text files that start with datafile
- `url -O http://www.website.com/datafile.txt[001-100]`: dl datafile001.txt to datafile100.txt
- `url -O http://www.website.com/datafile.txt[001-100:10]`: dl every tenth file from datafile001.txt to datafile100.txt

### Downloading data using wget
syntax: wget [option flags] [URL]<br>
URL is required. `curl` also supports `HTTP`, `HTTPS`, `FTP` and `SFTP`

optional flags unique to wget:<br>
- `-b`: download in the background
- `-q`: turn off the wget output
- `-c`: resume broken download

```bash
# option flags to dl in background and resume dl
wget -c -b https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Verify that the Spotify file has been downloaded
ls

# Preview the log file to see if dl successfully or if any errors
cat wget-log
```
**downloading multiple files**<br>
save multiple file locations in a list and use that to dl files.<br>
`wget -i url_list.txt`

to add constraints to downloads:
- `--limit-rate={rate}k`: limit the bandwidth usage, where `rate` is an integer.
- `--wait={n}`: pause n seconds after every file downloaded. useful for smaller files where the rate-limit isn't really useful.


## Data Processing at the command line
### csvkit
install/upgrade: `pip install --upgrade csvkit`

```bash
# Use ls to find the name of the zipped file
ls

# Use Linux's built in unzip tool to unpack the zipped file
unzip SpotifyData.zip

# Check to confirm name and location of unzipped file
ls

# Print all sheet names in SpotifyData.xlsx
in2csv -n SpotifyData.xlsx

# Convert "Worksheet1_Popularity" of SpotifyData.xlsx to csv
in2csv SpotifyData.xlsx --sheet "Worksheet1_Popularity" > SpotifyData.csv

# Print a preview in console using a csvkit suite command
csvlook SpotifyData.csv

# Print stats
```
### csvcut - filter columns
to print the list of headers in a file
- `csvcut -n <filename.csv>`

return columns by position or name
- `csvcut -c "track_id","name","album" songs.csv`
- `csvcut -c 1,3,4 songs.csv`
Note: names are in "double quotes" and multiple columns are seperated by a comma with no spaces.

### csvgrep - filter data by row
filters by row using exact match or regex fuzzy matching<br>
must be paired with on of these options:
- `-m` exact row value to filter
- `-r` regex pattern `csvgrep -c phone_number -r "555-555-\d{4}" data.csv > new.csv`
- `-f` path to file

### csvstack - stacking multiple csv files.
`csvstack file1.csv file2.csv > appendedfile.csv`
to know source of each row use `-g` with identifier for each source (in order of stacking)
- `csvstack -g "source1","source2" file1.csv file2.csv > appendedfile.csv`
- creates another column named "group" with each value identifying the source
To rename the "group" column heading:
- `csvstack -g "source1","source2" -n "source" file1.csv file2.csv > appendedfile.csv`
### chaining commands using operators
- `;`: runs commands sequentially
- - `csvlook file1.csv; csvlook file2.csv`
- `&&`: only run secnod command if first is successful
- - `csvlook file13.csv && csvstat file13.csv`
- `|`: 'pipe' output of first command as input to second commmand
- - `csvcut -c 1,3,4,7 file23.csv | csvlook`
- `>` save output of previous command to file
- - csvsort -c 2 file47.csv | head -n 15 > file47_Top15.csv


## Pulling data from command line
### sql2csv
syntax:
```bash
sql2csv --db "sqlite:///201812SpotifyDatabase.db" \
        --query "SELECT * FROM song_popularity" \
        > Spotify_song_Popularity.csv
```
- The db connection is dependent on the type of  database
- The query string (SQL command) has to be on one line, regardless of length
- not redirecting to file will print results in the terminal


### csvsql
- applies SQL statements to one or more csv files
- creates an in-memory SQL database that temporarily hosts file being processed
- therefore suatable for small to medium file sizes only
- SQL query must be written in one line
- file is referenced as a table (without the extensions)
- the file given must be pathed relative to working directory
- if using multiple files (via joins), the files must e listed in order of appearance in SQL
```bash
# query csv file using SQL syntax
csvsql --query "SELECT * FROM file1 ORDER BY col3 LIMIT 3" \
      file1.csv | csvlook

# using multiple files by join
csvsql --query query "SELECT * FROM file1 ORDER BY col3 LIMIT 3" \
       file1.csv file5.csv > joinedFile.csv
```
SQL queries can be long and complex. Another way is to save the query in a shell variable, then pass the variable in place of writing out statement in full.<br>
leads to less errors and easy readability
```bash
sqlquery="SELECT * FROM file1 ORDER BY col3 LIMIT 3"
csvsql --query "$sqlquery" file1.csv | csvlook
```

## pushing data back to database
using `csvsql` you can insert data into db
- `--db sqlite:///databse.db` important
- `--insert filename.csv` the insert flag will create table and insert data also infer shema type of table
- optional flags:
- - `--no-inference` data type will not be inferred and all data will be uploaded as strings
- - `--no-constraints` generate shema with no length limits or null checks
