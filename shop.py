store = {
    "coffee": {
            "price": 10,
            "inventory": 20
                },

    "tea": {
            "price": 5,
            "inventory": 15
            },

    "chocolate": {
            "price": 7,
            "inventory": 10
                    },

    "bread": {
            "price": 3,
            "inventory": 25
                },

    "milk": {
            "price": 6,
            "inventory": 12
            }
}

cart = {}

print("Products available in the store : ")
for product in store:
    price = store[product]["price"]
    print("-", product, "(price:", price, ")")

while True:
    product_name = input("Enter the name of the product (press enter to complete the purchase) : ")

    if product_name == "":
        break


    if product_name in store:
        quantity = int(input("Enter the required number : "))
        if quantity <= store[product_name]["inventory"]:
            price = store[product_name]["price"]
            total_price = price * quantity
            
            if product_name in cart:
                cart[product_name] += quantity
            else:
                cart[product_name] = quantity

            store[product_name]["inventory"] -= quantity

            print(f"Added to cart {product_name} ، number of {quantity}")
            print("all price : ", total_price)
        else:
            print("no mojodi")
    else:
        print("no mahsool in shop")

print("cart shop :")
for product in cart:
    quantity = cart[product]
    price = store[product]["price"]
    total_price = price * quantity
    print("-", product, "(number:", quantity, "price:", total_price, ")")