from models import AImodel
from exceptions import InvalidModalError, InvalidTemperatureError
from utils import log
from utils import load

load()

model = AImodel("llama", 1.4)

log("Model loaded successfully")

model.show_info()
model.generate("What is 2+2?")