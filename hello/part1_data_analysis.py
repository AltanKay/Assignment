productsAndPrices = {
    "pen":5.00,
    "pencil":3.00,
    "sharpener":2.50,
    "eraser":2.00,
    "Stilo":6.75
    }
quantities = {
    "pen":50,
    "pencil":80,
    "sharpener":40,
    "eraser":45,
    "Stilo":10
}
total_rev = 0
for product, price in productsAndPrices.items():
    quantity = quantities.get(product, 0)
    total_rev += price * quantity

print(f"Total Revenue: €{total_rev:.2f}")