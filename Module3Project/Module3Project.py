# Ice Cream Shop Application
# Author: Zakaria Mohamed
# Date: 01/29/2025

# Store our ice cream shop's menu items
from http.client import PARTIAL_CONTENT

# Add three new ice cream flavors to the flavors list
flavors = ["vanilla", "caramel", "mint", "chocolate", "strawberry", "coffee"]
toppings =["sprinkles", "nuts", "cherry"]
prices = {
    "scoop": 2.50,
    "topping": 0.50,

    # New cone prices added for Part 2
    "cake_cone": 0.50,    # Basic cone option
    "sugar_cone": 0.75,   # Medium-priced cone
    "waffle_cone": 1.50   # Premium cone option
}

# Modified function for Part 2: Added cone options and discount info
def display_menu():
    """Shows available flavors and toppings to the customer"""
    print("\n=== Welcome to the Ice Cream Shop! ===")
    print("\nAvailable Flavors:")
    for flavor in flavors:
        print(f"- {flavor}")
    
    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
    # New: Display cone options
    print("\nCone Options:")
    print(f"- Cake Cone: ${prices['cake_cone']:.2f}")
    print(f"- Sugar Cone: ${prices['sugar_cone']:.2f}")
    print(f"- Waffle Cone: ${prices['waffle_cone']:.2f}")
    
    print("\nPrices:")
    print(f"Scoops: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['topping']:.2f} each")
    # New: Display discount information
    print("\nSpecial: 10% discount on orders over $10!")

def get_flavors():
    """Gets ice cream flavor choices from the customer"""
    chosen_flavors = []

    # Use a while loop to keep taking orders until the customer is done
    while True:
        try:
            # Prompt the user to choose their scoops of ice cream
            num_scoops = int(input("\nHow many scoops would you like? (1-3): "))
            # Validate the input 
            if 1 <= num_scoops <= 3:
                break
            print("Please choose between 1 and 3 scoops.")
        except ValueError:
            print("Please enter a number.")
    
    # Prompt the user to enter the ice cream flavor
    print("\nFor each scoop, enter the flavor you'd like:")
    for i in range(num_scoops): #For loop prompts for each scoop of ice cream
        # Nested while loop handles the user's input and validation
        while True:
            flavor = input(f"Scoop {i+1}: ").lower()
            # Check to see if the flavor is one that's in the shop's list
            if flavor in flavors:
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor isn't available.")
    
    # Return to the calling function, the number of scoops the user wants
    # and the flavors they picked
    return num_scoops, chosen_flavors

def get_toppings():
    chosen_toppings = []

    # Use a while loop to prompt the user for the toppings until they
    #  are done adding toppings
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()
        #Test if the user is done ordering toppings
        if topping == 'done':
            break
        # Test if the topping is in the list of toppings for our shop
        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping isn't available.")

    # Return the list of toppings that the user chose
    return chosen_toppings

# Modified function for Part 2: Added cone cost and discount feature
def calculate_total(num_scoops, num_toppings, cone_type):
    """Calculates the total cost of the order with discount"""
    # Calculate individual costs
    scoop_cost = num_scoops * prices["scoop"]
    topping_cost = num_toppings * prices["topping"]
    cone_cost = prices[cone_type]  # New: Add cone cost
    
    # Calculate subtotal
    subtotal = scoop_cost + topping_cost + cone_cost
    
    # Apply 10% discount if order is over $10
    if subtotal > 10:
        discount = subtotal * 0.1
        return subtotal - discount
    return subtotal

# Modified function for Part 2: Added cone type and discount display
def print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_type):
    """Prints a nice receipt for the customer"""
    print("\n=== Your Ice Cream Order ===")
    # New: Display cone type
    print(f"Cone Type: {cone_type.replace('_', ' ').title()}")
    
    # Display scoops
    for i in range(num_scoops):
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}")
    
    # Display toppings if any
    if chosen_toppings:
        print("\nToppings:")
        for topping in chosen_toppings:
            print(f"- {topping.title()}")
    
    # Calculate total and show discount if applicable
    subtotal = calculate_total(num_scoops, len(chosen_toppings), cone_type)
    if subtotal > 10:
        original_total = subtotal / 0.9
        savings = original_total - subtotal
        print(f"\nOriginal Total: ${original_total:.2f}")
        print(f"You saved: ${savings:.2f} with our discount!")
    
    print(f"\nFinal Total: ${subtotal:.2f}")
    
    # Save order to file
    with open("daily_orders.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops - ${subtotal:.2f}")

# New function for Part 2: Search flavor feature
def search_flavor():
    """Allows customers to search for their favorite flavor"""
    # Get user's search input
    search = input("\nEnter the flavor you're looking for: ").lower()
    # Check if flavor is available
    if search in flavors:
        print(f"Good news! We have {search} in stock!")
        return True
    else:
        print(f"Sorry, we don't have {search} at the moment.")
        return False        

# New function for Part 2: Cone selection feature
def get_cone_choice():
    """Gets the customer's cone preference"""
    while True:
        # Display cone options
        print("\nChoose your cone type:")
        print("1. Cake Cone")
        print("2. Sugar Cone")
        print("3. Waffle Cone")
        choice = input("Enter your choice (1-3): ")
        
        # Return appropriate cone type based on choice
        if choice == "1":
            return "cake_cone"
        elif choice == "2":
            return "sugar_cone"
        elif choice == "3":
            return "waffle_cone"
        else:
            print("Please enter a valid choice (1-3)")

# Modified function for Part 2: Added flavor search and cone selection
def main():
    """Runs our ice cream shop program"""
    display_menu()
    
    # New: Add flavor search option
    while True:
        search = input("\nWould you like to search for a specific flavor? (yes/no): ").lower()
        if search == "yes":
            search_flavor()
        elif search == "no":
            break
    
    num_scoops, chosen_flavors = get_flavors()
    chosen_toppings = get_toppings()
    cone_type = get_cone_choice()  # New: Get cone selection
    print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_type)

# Automatically execute the main function when the application runs
if __name__ == "__main__":
    main()




