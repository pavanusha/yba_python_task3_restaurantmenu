def display_menu(menu):
    print("\nRestaurant Menu:")
    for item, price in menu.items():
        print(f"{item:20} - ₹{price:.2f}")
def take_order(menu):
    order = {}
    normalized_menu = {key.lower(): key for key in menu}
    try:
        while True:
            item = input("\nEnter the name of the item to order (or type 'done' to finish): ").strip().lower()
            if item == 'done':
                break
            elif item in normalized_menu:
                original_item = normalized_menu[item]
                quantity = input(f"Enter the quantity of {original_item}: ").strip()
                if quantity.isdigit() and int(quantity) > 0:
                    order[original_item] = order.get(original_item, 0) + int(quantity)
                else:
                    print("Invalid quantity. Please enter a positive number.")
            else:
                print("Item not found in the menu. Please choose a valid item.")
    except OSError:
        print("Error: Interactive input is not supported in this environment.")
        print("Please run this program in a local Python environment for full functionality.")
    return order

def calculate_bill(order, menu):
    """Calculate the total bill for the order."""
    total = 0
    print("\nYour Order Summary:")
    for item, quantity in order.items():
        price = menu[item] * quantity
        total += price
        print(f"{item:20} x {quantity} = ₹{price:.2f}")
    print(f"\nTotal Bill: ₹{total:.2f}")
    return total
def main():
    menu = {
        'Pasta': 249,
        'Pizza': 199,
        'Burger': 109,
        'Salad': 89,
        'Soup': 79,
        'Soda': 29
    }
    for item in menu:
        menu[item] = menu[item] 
    display_menu(menu)
    order = take_order(menu)
    if order:
        calculate_bill(order, menu)
    else:
        print("\nNo items were ordered. Thank you for visiting!")

if __name__ == "__main__":
    main()
