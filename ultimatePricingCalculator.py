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

### Helpers

def formatMoney(money):
    
    return f"${money:>6.2f}"

def formatMoneyForBusiness(money):
    # Business rules
    # Round to nearest 50 cents
    money = round(.5 * math.ceil(money/.5), 2)
    
    return formatMoney(money)

# format for table
def formatTable(description, records):
    fields = [desc[0] for desc in description]
    table = tabulate([fields] + records)

    return table

### Calculate Price

executescript("create_view.sql")
productInfo = cursor.execute("SELECT * FROM ProductInformation;").fetchall()
fields = cursor.description
table = formatTable(fields, productInfo)
print(table)

connection.close()