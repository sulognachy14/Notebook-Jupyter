# Online Shopping Cart and Billing System

# Product catalog
products = {
    101: {"name": "Notebook", "price": 100, "stock": 20},
    102: {"name": "Pen", "price": 20, "stock": 50},
    103: {"name": "Backpack", "price": 800, "stock": 10},
    104: {"name": "Headphones", "price": 1500, "stock": 5}
}

# Function to calculate discount
def calculate_discount(total):
    if total < 1000:
        return 0
    elif total < 3000:
        return total * 0.05
    else:
        return total * 0.10

# Function to generate bill
def generate_bill(cart):
    total = 0
    unique_ids = set(cart.keys())

    print("\n------ SHOPPING BILL ------")

    for pid in unique_ids:
        quantity = cart[pid]

        if pid not in products:
            print("Invalid product ID:", pid)
            continue

        product = products[pid]

        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            print("Invalid quantity for:", product["name"])
            continue

        if quantity > product["stock"]:
            print("Insufficient stock for:", product["name"])
            continue

        amount = product["price"] * quantity
        total += amount

        print(product["name"], "-", quantity, "x",
              product["price"], "=", amount)

    discount = calculate_discount(total)
    after_discount = total - discount
    gst = after_discount * 0.18
    final_amount = after_discount + gst

    print("Subtotal: Rs.", total)
    print("Discount: Rs.", round(discount, 2))
    print("GST (18%): Rs.", round(gst, 2))
    print("Final Bill: Rs.", round(final_amount, 2))


# Test Case 1: Below Rs.1000
cart1 = {101: 2, 102: 5}
print("\nTEST CASE 1")
generate_bill(cart1)

# Test Case 2: Rs.1000 to Rs.2999
cart2 = {103: 2, 101: 3}
print("\nTEST CASE 2")
generate_bill(cart2)

# Test Case 3: Rs.3000 and above
cart3 = {104: 2, 103: 1}
print("\nTEST CASE 3")
generate_bill(cart3)
