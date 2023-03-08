import discord as disc, json, requests, time as Time, asyncio
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
        print(id, msg)
        return await ctx.send(f"<@{id}> {msg}")
    await asyncio.sleep(2)
    return await checkifCTM(ctx, time, msg, id)

async def strCompare(client, idORname):
    Dict = {}
    for user in client.get_all_members():
        index = 0 
        score = 0 
        if len(str(user)) == len(idORname):
            score + 1
        for letterU in str(user):
            if letterU in idORname:
                score += 1
            index += 1
            
        Dict[str(user)] = score
    return max(Dict, key=Dict.get)


