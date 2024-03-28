# Define product names and prices
products = {
    "cola": 1.50,
    "chips": 1.00,
    "candy": 0.75,
    "water": 1.50
}

# Function to display available products and their costs
def display_products():
    print("Available products:")
    for product, price in products.items():
        print(f"{product.capitalize()}: ${price:.2f}")

# Function to simulate vending machine
def vending_machine():
    total_money = 0.0

    while True:
        print("\nWelcome to the vending machine!")
        display_products()
        print(f"Total money inserted: ${total_money:.2f}")

        choice = input("\nEnter the product you want to buy (or 'exit' to quit): ").lower()

        if choice == 'exit':
            print(f"Exiting... Here is your remaining balance: ${total_money:.2f}")
            break

        if choice in products:
            price = products[choice]

            if total_money >= price:
                print(f"Dispensing {choice}...")
                total_money -= price
                print(f"Remaining balance: ${total_money:.2f}")

                # Calculate and dispense change if needed
                if total_money > 0:
                    print(f"Dispensing change: ${total_money:.2f}")
                    total_money = 0
                    break  # Stop vending process after dispensing change
            else:
                print("Insufficient funds. Please insert more money.")
        else:
            print("Invalid product.")

        insert_money = input("Insert money (enter amount in dollars, or '0' to cancel): ")
        if insert_money == '0':
            continue
        try:
            money = float(insert_money)
            total_money += money
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

if __name__ == "__main__":
    vending_machine()
