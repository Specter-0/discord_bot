import discord as disc, requests, json
from discord.ext import commands

intents = disc.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents = intents)

def get_joke():
    json_data = json.loads(requests.get("https://v2.jokeapi.dev/joke/Programming,Dark").text)
    quote = json_data['setup'] + " " + json_data['delivery']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return

    elif message.content.startswith("!joke"):
        await message.channel.send(get_joke())

    elif message.content.startswith("hello bot"):
        name = str(message.author)
        name = name[:-5]
        await message.channel.send(f"Hello {name} please go fuck yourself")     

@client.command()
async def embed(ctx):
    embed = disc.Embed(title = "Commands", description = "idk just someting yk", color = 0xFF5733)
    await ctx.send(embed = embed)

client.run("MTA4MjQyMTExNTk0ODkwNDQ4MQ.GBZQUI.ekLScAyTuqVHdlk5U-t7jkFXBluR1XrxBUXIvI")