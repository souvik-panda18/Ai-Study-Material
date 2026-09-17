# ===== API Practice =====

# 1. Get all items
# 2. Get item by ID
# 3. Create item
# 4. Update item
# 5. Delete item
# 6. Exit
from api_test import get_models,get_model_by_id,create_model,delete_model,Update_item

# menu options
def menu():
    print("===== API Practice =====")
    print("1. Get all items")
    print("2. Get item by ID")
    print("3. Create item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Exit")
if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            models, status_code = get_models()
            if models:
                print("Models:", models)
            else:
                print("Failed to fetch models. Status code:", status_code)
        elif choice == "2":
            model_id = input("Enter model ID: ")
            model, status_code = get_model_by_id(model_id)
            if model:
                print("Model:", model)
            else:
                print("Failed to fetch model. Status code:", status_code)
        elif choice == "3":
            data = {
                "title": input("Enter title: "),
                "body": input("Enter body: "),
                "userId": int(input("Enter user ID: "))
            }
            created_model, status_code = create_model(data)
            if created_model:
                print("Created Model:", created_model)
            else:
                print("Failed to create model. Status code:", status_code)
        elif choice == "4":
            model_id = input("Enter model ID to update: ")
            data = {
                "title": input("Enter new title: "),
                "body": input("Enter new body: "),
                "userId": int(input("Enter new user ID: "))
            }
            updated_model, status_code = Update_item(model_id, data)
            if updated_model:
                print("Updated Model:", updated_model)
            else:
                print("Failed to update model. Status code:", status_code)
        elif choice == "5":
            model_id = input("Enter model ID to delete: ")
            status_code, message = delete_model(model_id)
            print(message, "Status code:", status_code)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")