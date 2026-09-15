from dataclasses import dataclass
@dataclass
class ModelConfig:
    name: str
    provider: str
    temperature: float
    def __post_init__(self):
        if not 0 <= self.temperature <= 1:
            raise ValueError("Temperature must be between 0 and 1")

class LLM:
    def __init__(self, config):
        self.config = config

    def generate(self, prompt):
        print(
            f"Generating with {self.config.name}: {prompt}"
        )

class Gemeni(LLM):
    pass
class Claude(LLM):
    pass



class ModelManager:
    def __init__(self):
        self.models = {} #this is dict to hold all the models, with their name as key and the model instance as value
        self.active_model = None

    def register(self, llm):
        # add llm to self.models using its config.name as key
        self.models[llm.config.name] = llm
        pass

    def switch(self, name):
        # set self.active_model to the model matching `name`
        # raise ValueError if not found
        if name in self.models:
            self.active_model = self.models[name]
        else:
            raise ValueError(f"Model {name} not found")
        pass

    def list_models(self):
        # loop through self.models and print details
        for name, model in self.models.items():
            print(f"Model Name: {name}, Provider: {model.config.provider}, Temperature: {model.config.temperature}")
        pass

    def generate(self, prompt):
        # use self.active_model to generate
        if self.active_model:
            self.active_model.generate(prompt)
        # handle the case where no model is active yet
        else:
            raise ValueError("No active model selected")

gemini = Gemeni(ModelConfig(name="Gemeni", provider="Gemeni Inc.", temperature=0.7))
model_manager = ModelManager()
model_manager.register(gemini)
model_manager.switch("Gemeni")
model_manager.list_models()
model_manager.generate("Explain RAG")