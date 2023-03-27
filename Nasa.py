import requests
import json
import random as rn
from urllib.request import urlretrieve


api_key = "G2eNNcd2aYd8rLtlwNinPoqhzjM0y6njUHPcoAUl"


async def get_nasa_image():
    req = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
    data = json.loads(req.content)

    return data


async def get_EPIC_image(enhanced):
    if enhanced != None:
        imgtype = "enhanced"
    else:
        imgtype = "natural"
    req_url = f"https://epic.gsfc.nasa.gov/api/{imgtype}?api_key={api_key}"
    req = requests.get(req_url)

    data = json.loads(req.content)

    new_data = data[rn.randint(0, len(data) - 1)]
    image_req = urlretrieve(f"https://epic.gsfc.nasa.gov/api/{imgtype}/{new_data['image']}.png?api_key={api_key}")
    image = json.loads(image_req)
    print(image)
    return new_data, image

   