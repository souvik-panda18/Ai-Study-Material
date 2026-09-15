from datetime import datetime, time


def log(message):
    time = datetime.now().strftime("%H:%M:%S")

    print(f"[{time}] {message}")

def load():
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}]{" Loading model..."}")
