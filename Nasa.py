import requests
import json

api_key = "G2eNNcd2aYd8rLtlwNinPoqhzjM0y6njUHPcoAUl"

async def get_nasa_image():
    req = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
    data = json.loads(req.content)

    return data