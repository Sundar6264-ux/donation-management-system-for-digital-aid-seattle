from datetime import datetime

def register_donation(data):
    """
    Prompts the user for donation details and adds them to the data.
    Updates the inventory based on the new donation.
    Args:
        data (dict): The main data dictionary containing donations and inventory.
    """
    donor_name = input("Enter donor's name: ")

    donation_type = input("Enter donation type (e.g., food, clothing, money): ").lower()
    if not (donor_name and donation_type):
        print("Donor name/donation type cannot be empty.")
        return
    
    try:
        quantity = int(input("Enter quantity or amount: "))
        if quantity <= 0:
            print("\nQuantity/amount must be a positive number.")
            return
    except ValueError:
        print("\nInvalid quantity. Please enter a number.")
        return

    donation = {
        'donor': donor_name,
        'type': donation_type,
        'quantity': quantity,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Add the new donation record
    data['donations'].append(donation)
    
    # Update the inventory
    data['inventory'][donation_type] = data['inventory'].get(donation_type, 0) + quantity
    
    print(f"\n\nSuccessfully registered donation of {quantity} units of {donation_type} from {donor_name}.")
    
def distribute_donation(data):
    """
    Prompts the user for distribution details and updates the inventory.
    Args:
        data (dict): The main data dictionary containing donations and inventory.
    """
    available_types = list(data['inventory'].keys())
    if not available_types:
        print("No donation types are currently available in the inventory.")
        return
    print("Available donation types:")
    for donation_type in available_types:
        print(f"- {donation_type.capitalize()}")
        
    donation_type = input("Enter donation type to distribute: ").lower()
    
    # Check if the donation type exists in inventory
    if donation_type not in data['inventory'] or data['inventory'][donation_type] == 0:
        print(f"\n\nNo {donation_type} available in inventory.")
        return
        
    try:
        quantity = int(input("Enter quantity to distribute: "))
        if quantity <= 0:
            print("\nQuantity must be a positive number.")
            return
    except ValueError:
        print("\nInvalid quantity. Please enter a number.")
        return
        
    if quantity > data['inventory'][donation_type]:
        print(f"\n\nInsufficient stock. Current stock of {donation_type} is {data['inventory'][donation_type]}.")
        return
        
    # Update inventory after distribution
    data['inventory'][donation_type] -= quantity
    # Log the distribution event with type, quantity, and date
    distribution_record = {
        'type': donation_type,
        'quantity': quantity,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    data['distributions'].append(distribution_record)
    
    print(f"\nSuccessfully distributed {quantity} units of {donation_type}.")

def generate_inventory_report(data):
    """
    Prints a report of the current inventory status, grouped by donation type.
    """
    print("\n--- Current Inventory Report ---")
    if not data['inventory']:
        print("Inventory is empty.")
        return
        
    for item_type, quantity in data['inventory'].items():
        print(f"- {item_type.capitalize()}: {quantity} units")
    print("--------------------------------\n")
    
def generate_donor_report(data):
    """
    Prints a report summarizing total contributions from each donor.
    """
    donor_summary = {}
    for donation in data['donations']:
        donor = donation['donor']
        quantity = donation['quantity']
        donor_summary[donor] = donor_summary.get(donor, 0) + quantity
        
    print("\n--- Donor Contributions Report ---")
    if not donor_summary:
        print("\nNo donations have been registered yet.")
        return
        
    for donor, total_quantity in donor_summary.items():
        print(f"- {donor}: Total contributions of {total_quantity} units")
    print("------------------------------------")

def generate_distribution_report(data):
    """
    Prints a report of all distribution events.
    """
    print("\n--- Distribution Report ---")
    if not data['distributions']:
        print("\nNo distributions have been logged yet.")
        return
    
    for record in data['distributions']:
        print(f"- {record['date']}: {record['quantity']} units of {record['type']} were distributed.")
    print("----------------------------")