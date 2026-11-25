CREATE TABLE members (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50)
);

COPY members(id, name, role)
FROM '/csv/sample.csv'
DELIMITER ','
CSV HEADER;