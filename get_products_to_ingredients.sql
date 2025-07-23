--SELECT Products.productName, Ingredients.ingredientName FROM Products, Ingredients, ProductsIngredients
--Where ProductsIngredients.productId = Products.id
--AND ProductsIngredients.ingredientId = Ingredients.id;

SELECT * FROM Products;