import csv
from BTrees._OOBTree import OOBTree

our_dict = {}
our_btree = OOBTree()

def add_item_to_tree(id, item):
    our_btree.update({id: item})

def add_item_to_dict(id, item):
    our_dict.update({id: item}) 

def range_query_tree(min_price, max_price):
    return [item for _, item in our_btree.items(min_price, max_price)]

def range_query_dict(min_price, max_price):
    return [item for item in our_dict.values() if min_price <= float(item[3]) <= max_price]

with open('generated_items_data.csv', mode ='r') as file:
  csvFile = csv.reader(file)
  i = 0
  for lines in csvFile:
        i += 1
        if i == 1:
            continue
        
        add_item_to_dict(int(lines[0]), lines)
        add_item_to_tree(int(lines[0]), lines)

f = range_query_dict(0, 50)
print(f)