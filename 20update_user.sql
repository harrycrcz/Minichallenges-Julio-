CREATE TABLE Users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);


INSERT INTO Users (id, name) VALUES (1, 'Lionel Messi');


UPDATE Users
SET name = 'Rodrigo De Paul'
WHERE id = 1;
