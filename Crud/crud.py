# This is a simple command-line CRUD (Create, Read, Update, Delete) application.
# It manages a list of items stored in memory.

# --- Global Data Storage ---
# We'll use a list of dictionaries to simulate a database.
# Each dictionary represents an item and will have a unique 'id'.
items_db = []
next_id = 1 # To assign unique IDs to new items

# --- CRUD Operations ---

def create_item(name, description):
    """
    Creates a new item and adds it to the items_db.
    Assigns a unique ID to the new item.
    """
    global next_id
    new_item = {
        "id": next_id,
        "name": name,
        "description": description
    }
    items_db.append(new_item)
    next_id += 1
    print(f"Item '{name}' (ID: {new_item['id']}) created successfully.")
    return new_item

def read_items():
    """
    Reads and displays all items currently in the items_db.
    If no items exist, it prints a corresponding message.
    """
    if not items_db:
        print("No items found.")
        return []
    
    print("\n--- Current Items ---")
    for item in items_db:
        print(f"ID: {item['id']}, Name: {item['name']}, Description: {item['description']}")
    print("---------------------\n")
    return items_db

def update_item(item_id, new_name=None, new_description=None):
    """
    Updates an existing item identified by its ID.
    Allows updating either the name, description, or both.
    """
    found = False
    for item in items_db:
        if item['id'] == item_id:
            found = True
            if new_name:
                item['name'] = new_name
            if new_description:
                item['description'] = new_description
            print(f"Item ID {item_id} updated successfully.")
            return item
    if not found:
        print(f"Item with ID {item_id} not found.")
    return None

def delete_item(item_id):
    """
    Deletes an item from the items_db based on its ID.
    """
    global items_db
    initial_len = len(items_db)
    items_db = [item for item in items_db if item['id'] != item_id]
    if len(items_db) < initial_len:
        print(f"Item with ID {item_id} deleted successfully.")
        return True
    else:
        print(f"Item with ID {item_id} not found.")
        return False

# --- Command-Line Interface (CLI) ---

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- Simple CRUD App Menu ---")
    print("1. Create Item")
    print("2. Read Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")
    print("----------------------------")

def run_app():
    """Main function to run the CRUD application."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            create_item(name, description)
        elif choice == '2':
            read_items()
        elif choice == '3':
            try:
                item_id = int(input("Enter the ID of the item to update: "))
                new_name = input("Enter new name (leave blank to keep current): ")
                new_description = input("Enter new description (leave blank to keep current): ")
                
                # Only pass non-empty strings to the update function
                update_item(item_id, 
                            new_name if new_name else None, 
                            new_description if new_description else None)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '4':
            try:
                item_id = int(input("Enter the ID of the item to delete: "))
                delete_item(item_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# --- Run the application ---
if __name__ == "__main__":
    run_app()