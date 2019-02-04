**Clearcode Internship Task - Katowice**<hr>
**Project contains two tasks from Clearcode:**
- Web Crawler<br>
- CSV Report Processing
<hr>

**Start project:**
- clone repository
- create and activate virtual environment
- install requirements from requirements.txt
- run scripts
<hr>

**Web Crawler**<br>
Project contains `site_map` function that takes url as an input.
Result is a dictionary, which contains all found links as a keys and dictionary that is value, 
with title and set of links that this website includes.
Example output:
```{
'http://0.0.0.0:8000': {
'title': 'Index',
'links': {'http://0.0.0.0:8000/example.html', 'http://0.0.0.0:8000/site.html'}
},
‘'http://0.0.0.0:8000/site.html': {
'title': 'The Site',
'links': {'http://0.0.0.0:8000/site/subsite.html'}
},
'http://0.0.0.0:8000/example.html': {
'title': 'No links here',
'links': set()
}... 
```
<hr>



**CSV Report Processing**<br>
Project converts CSV files.<br>
Example input:
```
date,subdivision,impressions,ctr
01/21/2019,Fāryāb,919,0.67%
01/22/2019,Beroun,139,0.61%
```

output:<br>
```
2019-01-21,AFG,919,6
2019-01-22,CZE,139,1
```
Output rows are saved into another file (called `result.csv`), which should appear after the script has been executed