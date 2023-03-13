import discord as disc, functions as func, os, thehub as hub, wonderwords as ww, random as rn
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

intents = disc.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True
client = commands.Bot(command_prefix='!', intents = intents)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event 
async def on_command_error(ctx, error):
    await ctx.send(f"Error, fuck you do?: {error}")

@client.event
async def on_message(message):
    await client.process_commands(message)
    print("here")
    random = rn.randint(1, 2)

    if message.author == client.user:
        return

    elif random == 1:
        print("here")
        r = ww.RandomSentence()
        sentance = r.sentence()   
        await message.channel.send(sentance)   

@client.event
async def on_message(message):
    await client.process_commands(message)

    if message.author == client.user:
        return

    elif message.content.startswith("hello"):
        if message.author == "Specter#8073":
            await message.channel.send("Hello master")     
        name = str(message.author)
        name = name[:-5]
        r = ww.RandomWord()
        word = r.word(include_parts_of_speech = ["verb"])   
        await message.channel.send(f"Hello {name} please go {word} yourself")  

    if rn.randint(1, 5) == 1:
        w = ww.RandomSentence()
        s = w.bare_bone_with_adjective()
        await message.channel.send(s)     


@client.command()
async def embed(ctx):
    embed = disc.Embed(title = "testing embeds", description = "mby some text here", color = 0xFF5733)
    embed.set_footer(text = "i am at the bottom")
    embed.set_image(url = "https://i.imgur.com/B5eGX2M.png")
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
    await ctx.send("koden her funket på et tidspunkt men har blit ødelakt av en opptatering idrk")
    """
    try:
        await ctx.send("ask a question")
        message = await client.wait_for("message", check = lambda message: message.author == ctx.author, timeout=30) # 30 seconds to reply
        await ctx.send("working...")
        print("question >>>", message.content)
        text = await get_chatgpt_text(str(message.content))
        await ctx.send(text)

    except asyncio.TimeoutError:
        await ctx.send("type faster bitch") 

    except disc.errors.HTTPException as error:
        if error.code == 50035:
            await ctx.send(f"{text[:1900]} \n \nthis reply was cut down due to being to fucking long")
        print(error.__context__, "\n", error, "\n", error.code)

    except disc.errors.ConnectionClosed or disc.errors.ClientException:
        await ctx.send("Could not connect to open-ai servers")
    """

@client.command()
async def LukasLT(ctx , time, *, msg = "gå å legg deg"):
    id = 282928626431688704
    await func.checkifCTM(ctx, time, msg, id)

@client.command()  
async def custom_timed_message(ctx , time, idORname, *, msg):
    try:
        int(idORname)
    except:
        for user in client.get_all_members():
            if str(user) == idORname:
                id = user.id
            elif str(user)[:-5] == idORname:
                id = user.id
    else:
        id = idORname

    try:
        await func.checkifCTM(ctx, time, msg, id)
    except UnboundLocalError:
        await ctx.send(f"{idORname} not found, where you looking for {await func.strCompare(client, idORname)}?")

@client.command()  
async def hub_get_star(ctx):
    star = await hub.get_star()
    embed = disc.Embed(title = star["name"], color = 0xFF5733)
    embed.set_image(url = star["photo"])
    await ctx.send(embed = embed)

client.run(os.environ.get('Discord-Api-Token'))