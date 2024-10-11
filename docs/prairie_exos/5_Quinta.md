# 5_Quinta

```sql
DROP DATABASE if EXISTS quinta_exo;
CREATE DATABASE quinta_exo;

DROP TABLE city, people;

\c quinta_exo;

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

INSERT INTO city (name, lat, lon)
VALUES ('Ilsan', 37.6, 126.7);
-- ON CONFLICT (name) DO NOTHING;

INSERT INTO city (name, lat, lon)
VALUES
('Gwacheon', 37.4, 126.9),
('Daegu', 35.8, 128.6),
('Gwangju', 35.1, 128.8),
('Busan', 35.1, 129.0);

INSERT INTO people(name, dob, height, city_id)
VALUES
('Kim Namjoon', '1994-09-12', 1.81, 1);

INSERT INTO people(name, dob, height, city_id)
VALUES
('Kim Seokjin', '1992-12-04', 1.79, 2),
('Min Yoongi', '1993-03-09', 1.74, 3),
('Jung Hoseok', '1994-02-18', 1.77, 4),
('Park Jimin', '1995-10-13', 1.75, 5),
('Kim Taehyung', '1995-12-30', 1.79, 3),
('Jeon Jungkook', '1997-09-01', 1.78, 5);

SELECT * FROM people;

SELECT * FROM people ORDER BY dob ASC;

SELECT * FROM people ORDER BY dob DESC;

SELECT people.name, people.dob, city.name 
FROM people
INNER JOIN city ON people.city_id = city.id;

--
SELECT people.name, people.dob, city.name 
FROM people
JOIN city ON people.city_id = city.id
GROUP BY city.name;

--
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