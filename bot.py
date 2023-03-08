import discord as disc, requests, json, asyncio, functions as func, os
from discord.ext import commands
from openai_bot import get_chatgpt_text
from dotenv import load_dotenv
load_dotenv()

intents = disc.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True
client = commands.Bot(command_prefix='!', intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#@client.event
#async def on_command_error(ctx, error):
    #await ctx.send(f"An error occured: {error}")

@client.event
async def on_message(message):
    await client.process_commands(message)
    
    if message.author == client.user:
        return

    elif message.content.startswith("hello"):
        name = str(message.author)
        name = name[:-5]
        await message.channel.send(f"Hello {name} please go fuck yourself")     


@client.command()
async def embed(ctx):
    embed = disc.Embed(title = "Commands", description = "idk just someting yk", color = 0xFF5733)
    await ctx.send(embed = embed)

@client.command()
async def joke(ctx):
    await ctx.send(func.get_joke())

@client.command()
async def annoy(ctx):
    await ctx.send("alvar gjore at denne ikke funker lenger")
    #for i in range(10):
        #await ctx.send("@everyone")

@client.command()
async def question(ctx):
    try:
        await ctx.send("ask a question")
        message = await client.wait_for("message", check = lambda message: message.author == ctx.author, timeout=30) # 30 seconds to reply
        await ctx.send("working...")
        print("question >>>", message.content)
        text = get_chatgpt_text(str(message.content))
        await ctx.send(text)

    except asyncio.TimeoutError:
        await ctx.send("type faster bitch") 

    except disc.errors.HTTPException as error:
        if error.code == 50035:
            await ctx.send(f"{text[:1900]} \n \nthis reply was cut down due to being to fucking long")
        print(error.__context__, "\n", error, "\n", error.code)

    except disc.errors.ConnectionClosed:
        await ctx.send("Could not connect to open-ai servers")
    
    except disc.errors.ClientException:
        print("ran here")

@client.command()
async def LukasLT(ctx , thyime, *, msg = "gå å legg deg"):
    id = 282928626431688704
    await func.checkifCTM(ctx, thyime, msg, id)

@client.command()  
async def custom_timed_message(ctx , thyime, idORname, *, msg):
    try:
        int(id)
    except:
        pass
    else:
        id = idORname

    for user in client.get_all_members():
        if str(user) == idORname:
            id = user.id
        elif str(user)[:-5] == idORname:
            id = user.id

    try:
        await func.checkifCTM(ctx, thyime, msg, id)
    except UnboundLocalError:
        await ctx.send(f"{idORname} not found, where you looking for {await func.strCompare(client, idORname)}?")

client.run(os.environ.get('Api-Token'))