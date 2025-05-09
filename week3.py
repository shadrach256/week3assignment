def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate and display the result
final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"Final price after {discount}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${original_price:.2f}")