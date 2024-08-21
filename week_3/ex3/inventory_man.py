inventory=[('item1',10),('item2',5),('item3',0),('item4',6)]
def check_inventory(a):
    for items,quantity in a:
        if quantity==0:
            print(items+" is out of stock")
check_inventory(inventory)
