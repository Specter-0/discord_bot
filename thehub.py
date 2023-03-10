import random as rn, pornhub 
from pornhub import PornHub as hub
client = hub()

async def get_star():
    for star in client.getStars(1, rn.randint(1, 100), False):
        return star
