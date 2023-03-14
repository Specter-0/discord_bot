import discord as disc, json, requests, asyncio
from datetime import datetime

def get_joke(): # using a joke api gets a randome joke with theme programming or dark
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
    return await checkifCTM(ctx, time, msg, id) # calls function again if its not yet time to send message

async def strCompare(client, name):
    long_name = {}
    for user in client.get_all_members(): # gets the longest name in the server
        long_name[(str(user))] = len(str(user))
    longest_name_len = len(max(long_name, key=long_name.get)) * -1

    Dict = {}
    for user in client.get_all_members(): # goes thro all members of a server and findes the closest name to idORname
        favor = 0 
        usable_name = name

        if len(str(user)[:-5]) == len(name): # might get removed as is pretty usless
            favor += 2

        for letterU in str(user):
            if letterU in usable_name:
                favor += 1
                usable_name = usable_name.replace(letterU, "", 1) # removes matching letter from name
            else: # if letter not in name
                favor -= 1 

        favor += longest_name_len + len(str(user)) # minuses favor by longest name - lenght of name
        Dict[str(user)] = favor 

    return max(Dict, key=Dict.get)

    


