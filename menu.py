# src/menu.py
from avl_tree import AVLTree

def main_menu():
    avl_tree = AVLTree()
    root = None

    while True:
        print("\n--- Smart City Route Planner ---")
        print("1. Add a new location")
        print("2. Remove a location")
        print("3. Display all locations")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            loc = input("Enter location name: ").strip()
            root = avl_tree.insert(root, loc)
            print(f"✅ Location '{loc}' added successfully.")

        elif choice == "2":
            loc = input("Enter location name to remove: ").strip()
            root = avl_tree.delete(root, loc)
            print(f"🗑️ Location '{loc}' removed successfully (if it existed).")

        elif choice == "3":
            print("\n📍 Current Locations:")
            print(avl_tree.inorder(root))

        elif choice == "4":
            print("👋 Exiting Smart City Route Planner...")
            break

        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
