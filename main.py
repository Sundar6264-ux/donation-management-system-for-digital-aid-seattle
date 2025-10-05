import data_manager
import donation_manager

def main():
    """
    The main function to run the donation management application.
    It displays a menu and handles user input.
    """
    data = data_manager.load_data()
    
    while True:
        print("\n--- Donation Management System Menu ---")
        print("#####   MAIN MENU   #####")
        print("1. Register a new donation")
        print("2. Distribute a donation")
        print("3. Reports")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            donation_manager.register_donation(data)
        elif choice == '2':
            donation_manager.distribute_donation(data)
        elif choice == '3':
            go_back_to_main = False
            while not go_back_to_main:
                print("#####   REPORTS   #####")
                print("1. Generate Inventory Report")
                print("2. Generate Donor Report")
                print("3. Generate Distribution Report")
                print("4. Main Menu")
                print("5. Exit")
                choice = input("Enter your choice (1-5): ")
                if choice == '1':
                    donation_manager.generate_inventory_report(data)
                elif choice == '2':
                    donation_manager.generate_donor_report(data)
                elif choice == '3':
                    donation_manager.generate_distribution_report(data)
                elif choice == '4': go_back_to_main = True
                elif choice == '5':
                    print("Exiting application. Saving data...")
                    data_manager.save_data(data)
                    return
        elif choice == '4':
            print("Exiting application. Saving data...")
            data_manager.save_data(data)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()