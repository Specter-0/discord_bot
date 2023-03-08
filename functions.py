import json, requests, time as Time, asyncio
from datetime import datetime

def get_joke():
    json_data = json.loads(requests.get("https://v2.jokeapi.dev/joke/Programming,Dark").text)
    if json_data["type"] == "twopart":
        quote = json_data['setup'] + " " + json_data['delivery']
    else:
        quote = json_data['joke']
    return(quote)

async def checkifCTM(ctx, time, msg, id):
    Stime = datetime.now()
    Ptime = Stime.strftime("%H:%M")
    print(Ptime)
    if Ptime >= time:
        return await ctx.send(f"<@{id}> {msg}")
    await asyncio.sleep(2)
    return await checkifCTM(ctx, time, msg, id)
