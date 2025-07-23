### SQL
import sqlite3

connection = sqlite3.connect('pricingCalculator.db')
cursor = connection.cursor()

def executescript(fileName:str, connection:sqlite3.Connection,  cursor:sqlite3.Cursor):
    with open(fileName, 'r') as sqlFile:
        sqlScript = sqlFile.read()
    
    cursor.executescript(sqlScript)
    connection.commit()

def execute(fileName:str, connection:sqlite3.Connection,  cursor:sqlite3.Cursor):
    with open(fileName, 'r') as sqlFile:
        sqlScript = sqlFile.read()
    
    cursor.execute(sqlScript)
    result = cursor.fetchall()
    
    connection.commit()
    
    return result

### Ingredients

#oz
weightIngredients = {
    "sugar": {
        "amount":400,
        "price":19.97
    }
}

#fl oz
volumeIngredients = {
    "corn syrup": {
        "amount":128,
        "price":19.99
    },
    "cinnamon oil": {
        "amount":0.125,
        "price":1.50
    },
    "food coloring": {
        "amount":0,
        "price":0
    }
}

### Packaging

packaging = { ###################################TODO: Include more for packaging (labels)
    "1oz": {
        "product":"Uline S-22824",
        "size":"2oz",
        "amount":10000,
        "price":92.00
    },
    "8oz": {
        "product":"Uline S-22827",
        "size":"6oz",
        "amount":5000,
        "price":85.00
    }
}

### Labor

desiredWage = 15.00

### Card/Surcharge

surchargePercent = 0.026
surchargeOffset = 0.10

### Desired Markup

markupPercent = 0.50

### Products

products = {
    "Cinnamon Skull": {
        "batch":18,
        "working hours":1,
        "weight": {
            "sugar":15
        },
        "volume": {
            "corn syrup":6,
            "cinnamon oil":0.25
        },
        "packaging":"1oz"
    },
    "Hard Tack": {
        "batch":2.25,
        "working hours":1,
        "weight": {
            "sugar":15
        },
        "volume": {
            "corn syrup":6,
            "cinnamon oil":0.25
        },
        "packaging":"8oz"
    }
}

### Helpers

def formatMoney(money):
    return f"{money:>5.2f}"

### Calculate Price

for item in products:
    
    currentProduct = products.get(item)
    pricePerBatch = 0.0
    
    measures = [["weight", weightIngredients], ["volume", volumeIngredients]]
    
    #per batch
    for measure in measures:
        
        currentMeasure = currentProduct.get(measure[0])
        
        for property in currentMeasure:
            usingAmount = currentMeasure.get(property)
            totalAmount = measure[1].get(property).get("amount")
            price = measure[1].get(property).get("price")
            
            pricePerBatch += (price/totalAmount) * usingAmount
    
    #per product
    pack = currentProduct.get("packaging")
    amount = packaging.get(pack).get("amount")
    price = packaging.get(pack).get("price")
    
    pricePerProduct = (price/amount)
    
    pricePerProduct += pricePerBatch/currentProduct.get("batch")
    
    laborPerProduct = (desiredWage * currentProduct.get("working hours"))/currentProduct.get("batch")
    
    basePerProduct = pricePerProduct + laborPerProduct
    
    totalPerProduct = basePerProduct + (basePerProduct * markupPercent)
    
    cardPrice = totalPerProduct + (pricePerProduct * surchargePercent) + surchargeOffset
    
    print("----------------------")
    print(item)
    print(f"Per Product:  ${formatMoney(pricePerProduct)}")
    print(f"Base (Labor): ${formatMoney(basePerProduct)}")
    print(f"Markup Total: ${formatMoney(totalPerProduct)}")
    print(f"Card Price:   ${formatMoney(cardPrice)}")

connection.close()