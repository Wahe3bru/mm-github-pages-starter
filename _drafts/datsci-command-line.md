
## Downloading data
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
