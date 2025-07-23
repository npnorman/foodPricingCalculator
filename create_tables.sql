DROP TABLE IF EXISTS Ingredients;
CREATE TABLE Ingredients (
    id integer PRIMARY KEY AUTOINCREMENT,
    ingredientName varchar(20),
    amount real,
    price real,
    measurement varchar(20)
);

DROP TABLE IF EXISTS Measurements;
CREATE TABLE Measurements (
    id integer PRIMARY KEY AUTOINCREMENT,
    measurement varchar(20),
    unit varchar(5)
);

DROP TABLE IF EXISTS PackagingItems;
CREATE TABLE PackagingItems (
    id integer PRIMARY KEY AUTOINCREMENT,
    item varchar(20),
    amount real,
    price real
);

DROP TABLE IF EXISTS PackagingSizes;
CREATE TABLE PackagingSizes (
    id integer PRIMARY KEY AUTOINCREMENT,
    size varchar(20)
);

DROP TABLE IF EXISTS PackagingSizesItems;
CREATE TABLE PackagingSizesItems (
    sizeId integer,
    itemId integer
);

DROP TABLE IF EXISTS Products;
CREATE TABLE Products (
    id integer PRIMARY KEY AUTOINCREMENT,
    productName varchar(20),
    batchSize real,
    workingHours real,
    packagingSize varchar(20)
);

DROP TABLE IF EXISTS ProductsIngredients;
CREATE TABLE ProductsIngredients (
    productId integer,
    ingredientId integer
);