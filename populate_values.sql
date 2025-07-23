INSERT INTO Products (productname,batchsize,workinghours, packagingsize) VALUES ('Cinnamon Skulls',18,1,'1oz');
INSERT INTO Products (productname,batchsize,workinghours, packagingsize) VALUES ('Hard Tack',2.25,1,'8oz');

INSERT INTO ProductsIngredients (productid, ingredientid) VALUES (1,1);
INSERT INTO ProductsIngredients (productid, ingredientid) VALUES (1,2);
INSERT INTO ProductsIngredients (productid, ingredientid) VALUES (1,3);
INSERT INTO ProductsIngredients (productid, ingredientid) VALUES (2,1);
INSERT INTO ProductsIngredients (productid, ingredientid) VALUES (2,2);
INSERT INTO ProductsIngredients (productid, ingredientid) VALUES (2,4);

INSERT INTO Ingredients (ingredientname, amount, price, measurement) VALUES ('sugar',400.0,19.97,'weight');
INSERT INTO Ingredients (ingredientname, amount, price, measurement) VALUES ('corn syrup',128.0,19.99,'volume');
INSERT INTO Ingredients (ingredientname, amount, price, measurement) VALUES ('cinnamon flavoring',0.125,1.50,'volume');
INSERT INTO Ingredients (ingredientname, amount, price, measurement) VALUES ('root beer flavoring',0.125,1.50,'volume');

INSERT INTO Measurements (measurement, unit) VALUES ('weight','oz');
INSERT INTO Measurements (measurement, unit) VALUES ('volume','fl oz');

INSERT INTO PackagingItems (item, amount, price) VALUES ('1oz Bags',10000,92.0);
INSERT INTO PackagingItems (item, amount, price) VALUES ('8oz Bags',5000,85.0);
INSERT INTO PackagingItems (item, amount, price) VALUES ('Front Label',270,8.12);
INSERT INTO PackagingItems (item, amount, price) VALUES ('Back Label',170,8.12);

INSERT INTO PackagingSizes (size) VALUES ('1oz');
INSERT INTO PackagingSizes (size) VALUES ('8oz');

INSERT INTO PackagingSizesItems (itemid, sizeid) VALUES (1,1);
INSERT INTO PackagingSizesItems (itemid, sizeid) VALUES (1,3);
INSERT INTO PackagingSizesItems (itemid, sizeid) VALUES (1,4);
INSERT INTO PackagingSizesItems (itemid, sizeid) VALUES (1,2);
INSERT INTO PackagingSizesItems (itemid, sizeid) VALUES (1,3);
INSERT INTO PackagingSizesItems (itemid, sizeid) VALUES (1,4);