from config import MODELS
from exceptions import InvalidModalError, InvalidTemperatureError

class AImodel:

    def __init__(self, name,temperature):
        self.name=name
        self.temperature=temperature

        self.validate_model()
        self.validate_temperature()

    def validate_model(self):
        if self.name not in MODELS:
            raise InvalidModalError(f"Invalid model name: {self.name}. Available models are: {', '.join(MODELS.keys())}")

    def validate_temperature(self):
        if not (0 <= self.temperature <= 2):
            raise InvalidTemperatureError(f"Invalid temperature: {self.temperature}. Temperature must be between 0 and 2.")

        maxtemperature = MODELS[self.name]["max temperature"]
        if self.temperature > maxtemperature:
            raise InvalidTemperatureError(
                f"Temperature for {self.name} cannot exceed {maxtemperature}."
            )

    def generate(self, prompt):
        # Placeholder for model generation logic
        print (f"Generated response for prompt: {prompt} using {self.name} at temperature {self.temperature}")
    
    def show_info(self):
        provider = MODELS[self.name]["provider"]

        print(f"Model: {self.name}")
        print(f"Provider: {provider}")
        print(f"Temperature: {self.temperature}")
