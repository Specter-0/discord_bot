import discord as disc, json, requests, asyncio
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
    if Ptime >= time:
        return await ctx.send(f"<@{id}> {msg}")
    await asyncio.sleep(2)
    return await checkifCTM(ctx, time, msg, id)

async def strCompare(client, name):
    long_name = {}
    for user in client.get_all_members():
        long_name[(str(user))] = len(str(user))
    longest_name_len = len(max(long_name, key=long_name.get)) * -1

    Dict = {}
    for user in client.get_all_members():
        favør = 0 
        usable_name = name

        if len(str(user)[:-5]) == len(name):
            favør += 2

        for letterU in str(user):
            if letterU in usable_name:
                favør += 1
                usable_name = usable_name.replace(letterU, "", 1)
            else:
                favør -= 1

        favør += longest_name_len + len(str(user))
        Dict[str(user)] = favør

    #print(Dict)
    return max(Dict, key=Dict.get)

    


