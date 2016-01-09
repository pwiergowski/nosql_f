#EDA

## Sprzet
Stacja robocza
- Intel i7-3770K 3.5GHz (8 rdzeni)
- 16 GB RAM DDR3 1600
- Dysk HDD
- Windows 7 Pro

VirtualBox Maszyna wirtualna Ubuntu 15.10
Przydzialone:
- 4 rdzenie 
- 8 GB RAM
- 250 GB przestrzeni dyskowej

## 1.Przygotowanie
Pobranie pliku [RC_2015-01.bz2](https://archive.org/download/2015_reddit_comments_corpus/reddit_data/2015/RC_2015-01.bz2)

## MongoDB (mongo)
```
#!bash
MongoDB shell version: 2.6.10
```
## PostgreSQL (psql)
```
#!bash
psql (PostgreSQL) 9.4.5
```
## 2.Importowanie danych
### MongoDB
Przejrzysty import do mongo z archiwum
```
#!bash
time bunzip2 -c RC_2015-02.bz2 | mongoimport --drop -d mongo -c reddit

connected to: 127.0.0.1
2015-12-10T09:41:12.189+0100 dropping: mongo.reddit
2015-12-10T09:41:15.010+0100 			36400	12133/second
.
.
.
2015-12-10T10:54:58.013+0100 			48311200	10915/second
2015-12-10T10:55:00.740+0100 check 9 48342747
2015-12-10T10:55:00.741+0100 imported 48342747 objects

real	73m48.577s
user	56m23.824s
sys	41m17.196s
```
![import_mongo.png](https://github.com/pwiergowski/nosql_f/blob/master/image/import_mongo.png)
Wykres pracy procesorów, wykres użycia pamięci operacyjnej
![import_mongo_disc_w7.png](https://github.com/pwiergowski/nosql_f/blob/master/image/import_mongo_disc_w7.png)
Zaobserwowane prędkości użycia dysku twardego
![import_mongo_disc_w7_g.png](https://github.com/pwiergowski/nosql_f/blob/master/image/import_mongo_disc_w7_g.png)
Wykres użycia dysku twardego


### PostgreSQL
Przed importem do bazy psql należy rozpakować archiwum, zajmuje to ok. 30 min. Po rozpakowaniu użyłem [pgfutter](https://github.com/lukasmartinelli/pgfutter) do zaimportowania danych do bazy psql.
```
#!bash
time ./pgfutter --db postgres --user postgres --pw 1234 json RC_2015-02
26.75 GB / 26.75 GB [==========================================] 100.00 % 35m37s
48342747 rows imported into import.rc_2015_02

real	35m37.611s
user	18m53.776s
sys	5m54.432s
```
![import_postgres.png](https://github.com/pwiergowski/nosql_f/blob/master/image/import_postgres.png)
Wykres pracy procesorów, wykres użycia pamięci operacyjnej
![import_postgres_w7.png](https://github.com/pwiergowski/nosql_f/blob/master/image/import_postgres_w7.png)
Zaobserwowane prędkości użycia dysku twardego, wykres użycia dysku twardego

## 3.Agregacje
### 3.1 Zliczanie wszystkich zaimportowanych obiektów
#### MongoDB
```
#!bash
time mongo mongo < mdb_count.js 
MongoDB shell version: 2.6.10
connecting to: mongo
48342747
bye

real	0m0.083s
user	0m0.028s
sys	0m0.028s
```

#### PostgreSQL

```
#!bash
time psql -U postgres -d postgres -c "SELECT count(*) FROM import.rc_2015_02;"
```
![psql_zlicznie.png](https://github.com/pwiergowski/nosql_f/blob/master/image/psql_zlicznie.png)

### 3.2 Ilosc rożnych subredditow 
#### MongoDB
```
#!bash
time mongo mongo < mdb_distinct_subreddit.js
```
![psql_zlicznie.png](https://github.com/pwiergowski/nosql_f/blob/master/image/mongo_distinct.png)

#### PostgreSQL
```
#!bash
time psql -U postgres -d postgres -c "SELECT COUNT(DISTINCT(data->>'subreddit')) FROM import.rc_2015_02;"

```



# GeoJSON

## Import MongoDB


```
#!bash
time mongoimport --drop -d geoj -c city < ~/Downloads/miasta.polski.json
connected to: 127.0.0.1
2015-12-13T01:23:27.903+0100 dropping: geoj.city
2015-12-13T01:23:28.230+0100 check 9 4100
2015-12-13T01:23:28.230+0100 imported 4100 objects

real	0m0.648s
user	0m0.084s
sys	0m0.048s

```

### Dzialania

#### Punkty

Wykonanie [geo1.js](https://github.com/pwiergowski/nosql_f/blob/master/pliki/geo1.js)

```
#!bash
mongo geo geo1.js

```
<script src="https://github.com/pwiergowski/nosql_f/blob/master/geojson/geo1result.geojson"></script>
