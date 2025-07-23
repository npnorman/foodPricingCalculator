INSERT INTO Products (productname,batchsize,workinghours, packagingSizeId) VALUES ('Cinnamon Skulls',18,1,1);
INSERT INTO Products (productname,batchsize,workinghours, packagingSizeId) VALUES ('Hard Tack',2.25,1,2);

INSERT INTO ProductsIngredients (productid, ingredientid, amount) VALUES (1,1, 15);
INSERT INTO ProductsIngredients (productid, ingredientid, amount) VALUES (1,2, 6);
INSERT INTO ProductsIngredients (productid, ingredientid, amount) VALUES (1,3, 0.25);
INSERT INTO ProductsIngredients (productid, ingredientid, amount) VALUES (2,1,15);
INSERT INTO ProductsIngredients (productid, ingredientid, amount) VALUES (2,2, 6);
INSERT INTO ProductsIngredients (productid, ingredientid, amount) VALUES (2,4,0.125);

INSERT INTO Ingredients (ingredientname, amount, price, measurementId) VALUES ('sugar',400.0,19.97,1);
INSERT INTO Ingredients (ingredientname, amount, price, measurementId) VALUES ('corn syrup',128.0,19.99,2);
INSERT INTO Ingredients (ingredientname, amount, price, measurementId) VALUES ('cinnamon flavoring',0.25,1.50,2);
INSERT INTO Ingredients (ingredientname, amount, price, measurementId) VALUES ('root beer flavoring',0.25,1.00,2);

INSERT INTO Measurements (measurement, unit) VALUES ('weight','oz');
INSERT INTO Measurements (measurement, unit) VALUES ('volume','fl oz');

INSERT INTO PackagingItems (item, amount, price) VALUES ('1oz Bags',10000,92.0);
INSERT INTO PackagingItems (item, amount, price) VALUES ('8oz Bags',5000,85.0);
INSERT INTO PackagingItems (item, amount, price) VALUES ('Front Label',270,8.12);
INSERT INTO PackagingItems (item, amount, price) VALUES ('Back Label',170,8.12);

INSERT INTO PackagingSizes (size) VALUES ('1oz');
INSERT INTO PackagingSizes (size) VALUES ('8oz');

INSERT INTO PackagingSizesItems (sizeid, itemid) VALUES (1,1);
INSERT INTO PackagingSizesItems (sizeid, itemid) VALUES (1,3);
INSERT INTO PackagingSizesItems (sizeid, itemid) VALUES (1,4);
INSERT INTO PackagingSizesItems (sizeid, itemid) VALUES (2,2);
INSERT INTO PackagingSizesItems (sizeid, itemid) VALUES (2,3);
INSERT INTO PackagingSizesItems (sizeid, itemid) VALUES (2,4);