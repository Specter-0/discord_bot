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
    if Ptime >= time:
        return await ctx.send(f"<@{id}> {msg}")
    await asyncio.sleep(2)
    return await checkifCTM(ctx, time, msg, id)

async def strCompare(client, idORname):
    long_name = {}
    for user in client.get_all_members():
        long_name[(str(user))] = len(str(user))
    longest_name_len = len(max(long_name, key=long_name.get)) * -1

    Dict = {}
    for user in client.get_all_members():
        score = 0 
        length = 0
        usable_idORname = idORname

        if len(str(user)[:-5]) == len(idORname):
            score += 2

        for letterU in str(user):
            try:
                if letterU in usable_idORname:
                    score += 1
                    usable_idORname = usable_idORname.replace(letterU, "", 1)
                else:
                    score -= 1
            except IndexError:
                print(user)
                score -= 2
            length += 1
        print(longest_name_len + length)
        score += longest_name_len + length
        Dict[str(user)] = score

    print(Dict)
    return max(Dict, key=Dict.get)


