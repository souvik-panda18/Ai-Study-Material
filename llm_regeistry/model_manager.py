import json


class Model:
    def __init__(self, name, provider, temperature):
        self.name = name
        self.provider = provider
        self.temperature = temperature

    def show(self):
        print(f"Name: {self.name}")
        print(f"Provider: {self.provider}")
        print(f"Temperature: {self.temperature}")


class ModelManager:
    def __init__(self):
        self.models = []

    def add_model(self, name, provider, temperature):
        model = Model(name, provider, temperature)
        self.models.append(model)

    def view_models(self):
        if not self.models:
            print("No models found.")
            return

        for model in self.models:
            model.show()
            print("----------------")

    def search_model(self, name):
        for model in self.models:
            if model.name.lower() == name.lower():
                model.show()
                return

        print("Model not found.")

    def delete_model(self, name):
        for model in self.models:
            if model.name.lower() == name.lower():
                self.models.remove(model)
                self.save_models()
                print("Model deleted.")
                return

        print("Model not found.")

    def save_models(self):
        data = []

        for model in self.models:
            data.append({
                "name": model.name,
                "provider": model.provider,
                "temperature": model.temperature
            })

        with open("models.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_models(self):
        try:
            with open("models.json", "r") as file:
                data = json.load(file)

            self.models = []

            for item in data:
                model = Model(
                    item["name"],
                    item["provider"],
                    item["temperature"]
                )

                self.models.append(model)

        except FileNotFoundError:
            self.models = []

        except json.JSONDecodeError:
            print("Invalid JSON file.")
            self.models = []