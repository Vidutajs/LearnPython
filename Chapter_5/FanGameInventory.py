stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems) :
    for item in addedItems :
        if item in inventory.keys() :
            inventory[item] += 1
        else:
            inventory.setdefault(str(item), 1)
    return inventory
    
stuff = addToInventory(stuff, dragonLoot)

displayInventory(stuff)


