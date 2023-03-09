import random as rn
from pornhub import PornHub as hub
client = hub()


async def get_star():
    for star in client.getStars(1, rn.randint(1, 100), False):
        return star

def get_video(*args):
    keywords = []
    for arg in args:
        keywords.append(arg)

    client = hub(keywords)

    for video in client.getVideos(1, 2):
        print("running...")
        print(video)
        print(video["url"])

#get_video("black")

client = hub("gay")

for video in client.getVideos(1, page=1):
    print("running...")
    print(video)
    print(video["url"])