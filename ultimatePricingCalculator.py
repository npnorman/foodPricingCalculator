import sqlite3
import math
from tabulate import tabulate

### SQL

connection = sqlite3.connect('pricingCalculator.db')
cursor = connection.cursor()

def executescript(fileName:str, connection:sqlite3.Connection=connection,  cursor:sqlite3.Cursor=cursor):
    with open(fileName, 'r') as sqlFile:
        sqlScript = sqlFile.read()
    
    cursor.executescript(sqlScript)
    connection.commit()

def execute(fileName:str, connection:sqlite3.Connection=connection,  cursor:sqlite3.Cursor=cursor):
    with open(fileName, 'r') as sqlFile:
        sqlScript = sqlFile.read()
    
    cursor.execute(sqlScript)
    result = cursor.fetchall()
    
    connection.commit()
    
    return result

### DB Setup

executescript("create_tables.sql")
executescript("populate_values.sql")

### Labor

desiredWage = 15.00

### Card/Surcharge

surchargePercent = 0.026
surchargeOffset = 0.10

### Desired Markup

markupPercent = 0.50

### Helpers

def formatMoney(money):
    
    return f"{money:>6.2f}"

def formatMoneyForBusiness(money):
    # Business rules
    # Round to nearest 50 cents
    money = round(.5 * math.ceil(money/.5), 2)
    
    return formatMoney(money)

# perCost -> float
def perCost(amount, price):
    # amount bought # if 0 => return 0
    # price bought at
    
    if amount == 0:
        return 0
    
    return price / amount

# format for table
def formatTable(description, records):
    fields = [desc[0] for desc in description]
    table = tabulate([fields] + records)

    return table

### Calculate Price

# for each product
products = cursor.execute("SELECT Products.productName, Products.id, Products.batchSize, Products.workingHours FROM Products").fetchall()
for product in products:
        
    pricePerBatch = 0
    pricePerProduct = 0
    perPackaging = 0
    perIngredient = 0
    
    (productName, productId, batchSize, workingHours) = product
        
    # batch cost
    sql = f"""
    SELECT ProductsIngredients.amount, Ingredients.amount, Ingredients.price
    FROM ProductsIngredients, Ingredients, Products
    WHERE ProductsIngredients.productId = Products.id
    AND ProductsIngredients.ingredientId = Ingredients.id
    AND Products.id = {productId}
    """
    ingredients = cursor.execute(sql).fetchall()
    # for each ingredient needed for the product
    for ingredient in ingredients:
        (amountUsed, amountBought, price) = ingredient
        # get amount used
        # perCost(amount, price) * amount used
        # add to pricePerBatch
        pricePerBatch += perCost(amountBought, price) * amountUsed
        
    # pricePerProduct = pricePerBatch / batch size
    perIngredient = pricePerBatch / batchSize
    pricePerProduct += perIngredient
    
    # packaging cost
    sql2 = f"""
    SELECT PackagingItems.amount, PackagingItems.price
    FROM PackagingItems, PackagingSizes, PackagingSizesItems, Products
    WHERE PackagingSizesItems.itemId = PackagingItems.id
    AND PackagingSizesItems.sizeId = PackagingSizes.id
    AND PackagingSizes.id = Products.packagingSizeId
    AND Products.id = {productId};
    """
    packagingItems = cursor.execute(sql2).fetchall()
    # for each packaging item needed for the product's packaging size
    for packagingItem in packagingItems:
        (amountBought, price) = packagingItem
        # get amount used (always 1)
        # perCost(amount, price) * amount used
        # add to pricePerProduct
        perPackaging += perCost(amountBought, price)
    pricePerProduct += perPackaging

    # Other
    
    # laborPerProduct = (desiredWage * workingHours) / batchSize
    
    # basePerProduct = pricePerProduct + laborPerProduct
    
    # totalPerProduct = basePerProduct + (basePerProduct * markupPercent)
    
    # cardPrice = totalPerProduct + (totalPerProduct * surchargePercent) + surchargeOffset

    print("----------------------")
    print(productName)
    print(f"Per Batch:          ${formatMoney(pricePerBatch)}")
    print(f"Per Ingredients:    ${formatMoney(perIngredient)}")
    print(f"Per Packaging:      ${formatMoney(perPackaging)}")
    print(f"Per Product:        ${formatMoney(pricePerProduct)}")
    # print(f"Labor Per Product:  ${formatMoney(laborPerProduct)}")
    # print(f"Product + Labor:    ${formatMoney(basePerProduct)} *")
    # print(f"Markup Total:       ${formatMoney(totalPerProduct)} *")
    # print(f"Card Price:         ${formatMoney(cardPrice)} *")

print("----------------------")
# print("* Formated for business rules\n")

executescript("create_view.sql")
productInfo = cursor.execute("SELECT * FROM ProductInformation;").fetchall()
fields = cursor.description
table = formatTable(fields, productInfo)
print(table)

connection.close()