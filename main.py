def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices



products = ["Apple", "Banana", "Orange", "Apple", "Mango", "Apple"]

target_product = "Apple"
indices = linear_search_product(products, target_product)

if indices:
    print("The product", target_product, "is found at indices:", indices)
else:
    print("The product", target_product, "is not found.")


