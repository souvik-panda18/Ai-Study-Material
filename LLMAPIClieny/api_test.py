
import requests

Base_url = ""
def get_models():
    response = requests.get(Base_url)
    if response.status_code == 200:
        return response.json(),response.status_code
    else:
        return None ,response.status_code

def get_model_by_id(model_id):
    response = requests.get(f"{Base_url}/{model_id}")
    if response.status_code == 200:
        return response.json(), response.status_code
    else:
        return None, response.status_code

def create_model(data):
    response = requests.post(Base_url, json=data)
    if response.status_code == 201:
        return response.json(), response.status_code    
    else:
        return None, response.status_code

def delete_model(model_id):
    response = requests.delete(f"{Base_url}/{model_id}")
    return response.status_code,"deleted successfully" if response.status_code == 200 else "failed to delete"

def Update_item(model_id,data):
    response=requests.put(f"{Base_url}/{model_id}", json=data)
    if response.status_code == 200:
        return response.json(),"response code:"+ str(response.status_code)
    else:
        return None, response.status_code



