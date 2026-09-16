from model_manager import ModelManager


manager = ModelManager()
manager.load_models()


while True:
    print("\n===== LLM Model Registry =====")
    print("1. Add model")
    print("2. View models")
    print("3. Search model")
    print("4. Delete model")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        print("\n--- Add Model ---")

        name = input("Model name: ")
        provider = input("Provider: ")

        try:
            temperature = float(input("Temperature: "))
        except ValueError:
            print("Temperature must be a number.")
            continue

        manager.add_model(name, provider, temperature)
        manager.save_models()

        print("Model added successfully.")

    elif choice == "2":

        print("\n--- Models ---")
        manager.view_models()

    elif choice == "3":

        print("\n--- Search Model ---")

        name = input("Enter model name: ")
        manager.search_model(name)

    elif choice == "4":

        print("\n--- Delete Model ---")

        name = input("Enter model name: ")
        manager.delete_model(name)

    elif choice == "5":

        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-5.")