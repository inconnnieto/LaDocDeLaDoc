# 5_Quinta

## brief

### my attempt

I worked with SQL to created a relational databse.

**Goal:**
create tables for cities and people 

you can check the repo exo [here.](https://gitlab.com/prairie-ia/prairie_exos/-/tree/main/5_Quinta?ref_type=heads)
### 1. Create a database
```sql
DROP DATABASE if EXISTS quinta_exo;
CREATE DATABASE quinta_exo;

DROP TABLE city, people;

\c quinta_exo;
```

### 2. Create table 
```sql
CREATE TABLE city(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    lat FLOAT,
    lon FLOAT
);

CREATE TABLE people(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    height FLOAT,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES city(id)
);

```
### 3. Inserting data into tables

#### add a city 

```sql

INSERT INTO city (name, lat, lon)
VALUES ('Ilsan', 37.6, 126.7);
-- ON CONFLICT (name) DO NOTHING;

INSERT INTO city (name, lat, lon)
VALUES
('Gwacheon', 37.4, 126.9),
('Daegu', 35.8, 128.6),
('Gwangju', 35.1, 128.8),
('Busan', 35.1, 129.0),
('Hanoi', 21.0285, 105.8542),
('Ho Chi Minh City', 10.8231, 106.6297),('Sydney', -33.8688, 151.2093);
```

#### add a person
```sql
INSERT INTO people(name, dob, height, city_id)
VALUES
('Kim Namjoon', '1994-09-12', 1.81, 1);
```
#### add x people at once
```sql
INSERT INTO people(name, dob, height, city_id)
VALUES
('Kim Seokjin', '1992-12-04', 1.79, 2),
('Min Yoongi', '1993-03-09', 1.74, 3),
('Jung Hoseok', '1994-02-18', 1.77, 4),
('Park Jimin', '1995-10-13', 1.75, 5),
('Kim Taehyung', '1995-12-30', 1.79, 3),
('Jeon Jungkook', '1997-09-01', 1.78, 5),
('Kim Minji', '2004-05-07', 1.63, 1),
('Phan Hanni', '2004-10-06', 1.64, 6),
('Danielle Marsh', '2005-04-11', 1.62, 7),('Jang Haerin', '2006-02-01', 1.61, 5),('Lee Hyein', '2008-04-21', 1.57, 4),
('Choi Yeonjun', '1999-09-13', 1.81, 3),('Choi Soobin', '2000-12-05', 1.80, 1),('Choi Beomgyu', '2002-03-13', 1.80, 3),('Kang Taehyun', '2002-02-05', 1.78, 4);
```
## SQL Queries
####  Récupérer la liste de toutes les personnes
```sql
SELECT * FROM people;
```

#### Récupérer la liste de toutes les personnes, triées de la plus vieille à la plus jeune
```sql
SELECT * FROM people ORDER BY dob ASC;
```
#### Récupérer la liste de toutes les personnes, trier de la plus petite à la plus grande.
```sql
SELECT * FROM people ORDER BY dob DESC;
```
#### Récupérer la liste de toutes les personnes, avec le nom de sa ville de naissance
```sql
SELECT people.name, people.dob, city.name 
FROM people
INNER JOIN city ON people.city_id = city.id;
```
#### Récupérer la liste de toutes les personnes, regroupés par villes
```sql
SELECT people.name, people.dob, city.name 
FROM people
JOIN city ON people.city_id = city.id
GROUP BY city.name;
```
#### Récupérer la liste de toutes les personnes, de celle qui est née le plus proche de Toulouse à celle qui est née le plus loin

The **Euclidean** distance formula approximates the straight-line distance between a city’s latitude and longitude and a fixed point.

![5_Quinta_formula](https://gitlab.com/prairie-ia/ma_doc/-/raw/mai/docs/imgs/5_Quinta_formula.PNG?ref_type=heads)

coordinates of Toulouse (43.6045° N, 1.4442° E) fixed and constant, multiplication by 111.11 converts the result from degrees to kilometers, assuming a roughly spherical Earth.

```sql
SELECT
    people.name,
    people.dob,
    city.name,
    city.lat,
    city.lon,
    SQRT(
        POWER((city.lon - 1.4442), 2) + POWER((city.lat - 43.6045), 2)
    ) * 111.11 AS distance_km
FROM people
JOIN city ON people.city_id = city.id
ORDER BY distance_km;
```

#### notes:
In this test application, the Euclidean distance formula is chosen for its simplicity, speed, and efficiency. 

Using a more accurate formula, (Haversine or Vincenty) would introduce unnecessary computational complexity at this stage, making it more suited for large-scale or production applications where precision is crucial and the computational overhead is acceptable.