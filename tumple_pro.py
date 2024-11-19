store_inventory_list=[
    ("laptop",5,30000.0),
    ("Headphone",15,500.00),
    ("Mouse",50,150.00),
    ("Keyboard",20,150.00),
    ("Monitor",10,3000.00)
]
highest_stock_value=0
item_with_highest_stock_value=0

for item in store_inventory_list:
    unit_item,quantity,unit_price=item
    stock_value=quantity*unit_price
    print(f"Item name:{unit_item},The Total value is: {stock_value}")
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=unit_item 
print(f"Highest stock value is : {highest_stock_value}")
print(f"Item with the highest stock value is : {item_with_highest_stock_value}")

