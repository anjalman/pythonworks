

product={"id":101,"title":"snikers","price":50,"brand":"nestle"}

# to update product price 

product["price"]=100

print(product["id"])

print(product["title"])

print(product["price"])

print(product["brand"])

product["offer"]=5

product["use_by_date"]= 12-2-2025

if "offer"in product:

    product["offer"]=10

else:

    product["offer"]=20
    
print(product)