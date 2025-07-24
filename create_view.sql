DROP VIEW IF EXISTS ProductInformation;
DROP VIEW IF EXISTS ProductBatchInfo;
DROP VIEW IF EXISTS ProductPackagingInfo;

CREATE VIEW ProductBatchInfo AS
SELECT DISTINCT
Products.id as 'id',
Products.productName AS 'Product',
ROUND(SUM((Ingredients.price / Ingredients.amount) * ProductsIngredients.amount),2) AS 'Price Per Batch',
ROUND(SUM(((Ingredients.price / Ingredients.amount) * ProductsIngredients.amount)) / Products.batchSize, 2) AS 'Price Per Ingredients'
FROM
Products,
Ingredients,
ProductsIngredients
WHERE ProductsIngredients.productId = Products.id
AND ProductsIngredients.ingredientId = Ingredients.id
GROUP BY Products.id;

CREATE VIEW ProductPackagingInfo AS
SELECT DISTINCT
Products.id as 'id',
Products.productName AS 'Product',
ROUND(SUM(PackagingItems.price / PackagingItems.amount), 2) AS 'Price Per Product Packaging'
FROM
Products,
PackagingItems,
PackagingSizes,
PackagingSizesItems
WHERE PackagingSizesItems.itemId = PackagingItems.id
AND PackagingSizesItems.sizeId = PackagingSizes.id
AND PackagingSizes.id = Products.packagingSizeId
GROUP BY Products.id; --may me miscalculating

CREATE VIEW ProductInformation AS
SELECT DISTINCT
Products.productName AS 'Product',
ProductBatchInfo.'Price Per Batch',
ProductBatchInfo.'Price Per Ingredients',
ProductPackagingInfo.'Price Per Product Packaging',
ProductBatchInfo.'Price Per Ingredients' + ProductPackagingInfo.'Price Per Product Packaging' AS 'Price Per Product'
FROM
Products,
ProductBatchInfo,
ProductPackagingInfo
WHERE Products.id = ProductBatchInfo.id
AND Products.id = ProductPackagingInfo.id
GROUP BY Products.id;