

## MongoDB (mongo)
```
#!bash
MongoDB shell version: 2.6.10
```
## Python (python)
```
#!bash
Python 2.7.10
```
## Przygotowanie
Pobranie pliku [RC_2015-01.bz2](https://archive.org/download/2015_reddit_comments_corpus/reddit_data/2015/RC_2015-01.bz2)

## Importowanie danych
```
#!bash
time bunzip2 -c RC_2015-02.bz2 | mongoimport --drop -d mongo -c reddit
```

## Ilosc rożnych subredditow 
##Agregation Pipeline
### JavaScript
Wykonanie [mdb_distinct_subreddit.js](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_distinct_subreddit.js)
```
#!bash
time mongo mongo < mdb_distinct_subreddit.js
```
![mongo_distinct.png](https://github.com/pwiergowski/nosql_f/blob/master/image/mongo_distinct.png)

### Python
Wykonanie [mdb_distinct_subreddit.py](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_distinct_subreddit.py)
```
#!bash
time python mdb_distinct_subreddit.py
```
![mdb_distinct_subreddit.png](https://github.com/pwiergowski/nosql_f/blob/master/image/mdb_distinct_subreddit.png)

## Map-Reduce
### JavaScript
Wykonanie [mdb_mr_distinct_subreddit.js](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_distinct_subreddit.js)
```
#!bash
time mongo mongo < mdb_mr_distinct_subreddit.js
```
![mdb_mr_distinct_subreddit.png](https://github.com/pwiergowski/nosql_f/blob/master/image/mdb_mr_distinct_subreddit.png)

### Python
Wykonanie [mdb_mr_distinct_subreddit.py](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_distinct_subreddit.py)
```
#!bash
time python mdb_mr_distinct_subreddit.py
```
![mdb_distinct_subreddit.png](https://github.com/pwiergowski/nosql_f/blob/master/image/mdb_mr_distinct_subreddit_py.png)

## Ilosci komentarzy w watku KerbalSpaceProgram
### JavaScript
Wykonanie [mdb_ksp_count.js](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_ksp_count.js)
```
#!bash
time mongo mongo < mdb_ksp_count.js
```

### Python
Wykonanie [mdb_ksp_count.py](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_ksp_count.py)
```
#!bash
time python mdb_ksp_count.py
```
![mdb_ksp_count.png](https://github.com/pwiergowski/nosql_f/blob/master/image/mdb_ksp_count.png)
wyniki python / mongo

## Autorzy najwiekszej ilosci komentarzy w watku KerbalSpaceProgram i srednia ocen tych komentarzy  
##Agregation Pipeline
### JavaScript
Wykonanie [mdb_ksp_top_10.js](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_ksp_top_10.js)
```
#!bash
time mongo mongo < mdb_ksp_top_10.js
```

### Python
Wykonanie [mdb_ksp_top_10.py](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_ksp_top_10.py)
```
#!bash
time python mdb_ksp_top_10.py
```
![mdb_ksp_top_10.png](https://github.com/pwiergowski/nosql_f/blob/master/image/mdb_ksp_top_10.png)
wyniki python / mongo

## Autorzy najgorzej ocenianych komentarzy w danym temacie (subreddicie). Najgorsza 20.
##Agregation Pipeline
### JavaScript
Wykonanie [mdb_bot_20_sub_aut.js](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_bot_20_sub_aut.js)
```
#!bash
time mongo mongo < mdb_bot_20_sub_aut.js
```

### Python
Wykonanie [mdb_bot_20_sub_aut.py](https://github.com/pwiergowski/nosql_f/blob/master/pliki/mdb_bot_20_sub_aut.py)
```
#!bash
time python mdb_ksp_top_10.py
```
![mdb_ksp_top_10.png](https://github.com/pwiergowski/nosql_f/blob/master/image/mdb_bot_20_sub_aut.png)
wyniki mongo / python



