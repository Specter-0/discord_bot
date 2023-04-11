import discord as disc, functions as func, os, wonderwords as ww, random as rn, Nasa
import chatgpt as Cgpt, asyncio
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from discord import Color as c
load_dotenv()

# intents needed to preform tasks
intents = disc.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True
intents.guilds = True 
intents.moderation = True
intents.bans = True
intents.guild_reactions = True
intents.integrations = True
intents.auto_moderation = True
intents.presences = True
client = commands.Bot(command_prefix='!', intents = intents) # command setup


@client.event # prints when bot has connected to discord / is online
async def on_ready():
    print('logged in as {0.user}'.format(client))

"""
@client.event # runs on any command error
async def on_command_error(ctx, error):
    await ctx.send(f"Error, fuck you do?: {error}")
"""

@client.event # preforms some actions on a message being sent by a user
async def on_message(message):
    await client.process_commands(message)

    if message.author == client.user or message.content.startswith("!"): # makes sure that the bot does not reply to its self or on command messages
        return

    elif message.content.startswith("hello"): 
        if message.author.id == 799265201026236437: # if author.id matches my id then it will reply
            await message.channel.send("Hello master!")
            return     

        name = str(message.author) # else it resonds with a partly randomly generated sentence
        name = name[:-5] # a discord name usally has a #xxxx behind it, this removes it
        r = ww.RandomWord()
        word = r.word(include_parts_of_speech = ["verb"]) # makes it only generate verbs
        await message.channel.send(f"Hello {name} please go {word} yourself")  

    if rn.randint(1, 20) == 1: # randomly sends a random sentence cuz why not
        w = ww.RandomSentence() # creats a RandomSentence object
        s = w.bare_bone_with_adjective()
        await message.channel.send(s)     


@client.command()
@commands.is_owner() # self explanatory 
async def shutdown(ctx):
    exit() # just exits the programm


@client.command() # more for testing purposes
async def embed(ctx):
    embed = disc.Embed(title = "testing embeds", description = "mby some text here", color = 0xFF5733) # setup
    embed.set_footer(text = "i am at the bottom") # appares at the bottom 
    embed.set_image(url = "https://i.imgur.com/B5eGX2M.png") # a picture
    await ctx.send(embed = embed) # sends embed to chat


@client.command() # using an api i get jokes 
async def joke(ctx):
    await ctx.send(func.get_joke()) # c function.py


@client.command() # self exlanatory
async def annoy(ctx):
    await ctx.send("alvar gjore at denne ikke funker lenger")
    #for i in range(10):
        #await ctx.send("@everyone")


@client.command() # sends in a question to chat gpt in a loop which will exit after 30 sec or by typing anything in ["exit", "Exit", "leave", "stop"]
async def question(ctx):
    await ctx.send("ask a question")
    while True:
        try:
            # waits for an awnser from the person who sent the !question 
            message = await client.wait_for("message", check = lambda message: message.author == ctx.author, timeout = 45) # 30 seconds to reply

            if message.content in ["exit", "Exit", "leave", "stop"]: # exits if anything in list content if typed
                await ctx.send("Exited")
                return

            await ctx.send("working...")
            print("question >>>", message.content)

            text = await Cgpt.get_chatgpt_text(str(message.content)) # sends the message to chat gpt file and waits for reply
            await ctx.send(text) # sends reply to chat

        except asyncio.TimeoutError: # if takes more then 45 sec to reply
            await ctx.send("Timeout exit") 
            return

        except disc.errors.HTTPException as error: # happends when the string sent back from chat gpt is over 2000 chars long
            if error.code == 50035:
                await ctx.send(f"{text[:1900]} \n \nthis reply was cut down due to being to fucking long")
            print(error.__context__, "\n", error, "\n", error.code)

        except disc.errors.ConnectionClosed: # if you have school internett or the cl is 12:00 these might happen
            await ctx.send("Could not connect to open-ai servers")
    

@client.command() # makes an alarm for when lukas needs to go to bed, only works with lukas
async def LukasLT(ctx , time, *, msg = "gå å legg deg"):
    id = 282928626431688704
    await func.checkifCTM(ctx, time, msg, id)


@client.command() # custom message that will be sent at a given time
async def custom_timed_message(ctx , time, idORname, *, msg):
    user = await func.find_user(ctx, client, idORname)
    if user == None:
        return
    await func.checkifCTM(ctx, time, msg, user.id)


@client.command()
async def move_vc(ctx, channel_idORname, *, idORname):
    await func.remove_user_message(ctx)
    user = await func.find_user(ctx, client, idORname)
    channel = await func.find_channel(client, channel_idORname)
    if channel == None:
        await ctx.send(f"{channel_idORname} not found") 
        return
    await user.move_to(channel)


@client.command()
async def nasa_daily_image(ctx):
    data = await Nasa.get_nasa_image()

    embed = disc.Embed(title = data["title"], description = data["explanation"], color = 0xFF5733) # setup
    embed.set_footer(text = data["date"])
    embed.set_image(url = data["hdurl"]) 
    await ctx.send(embed = embed) 


@client.command()
async def EPIC(ctx, enhanced = None):
    data = await Nasa.get_EPIC_image(enhanced)

    embed = disc.Embed(title = "EPIC image", description = data["caption"], color = 0xFF5733) # setup
    embed.set_footer(text = data["date"])
    embed.set_image(url = data["image"]) 
    await ctx.send(embed = embed) 


@client.command()
@commands.is_owner()  
async def GSA(ctx): 
    await func.remove_user_message(ctx)

    guild = await func.get_guild(ctx, client)
    member = guild.get_member(799265201026236437)
    role = get(ctx.guild.roles, id=1084769739693367331)

    await member.add_roles(role)


@client.command()
@commands.is_owner()  
async def create_role(ctx, role_name, assign_id): 
    await func.remove_user_message(ctx)

    guild = await func.get_guild(ctx, client)
    member = guild.get_member(int(assign_id))
    role = await guild.create_role(name = role_name, color = c.random(), permissions = disc.Permissions.all())

    await member.add_roles(role)


@client.command()
@commands.is_owner()  
async def get_roles(ctx): 
    await func.remove_user_message(ctx)
    for role in ctx.guild.roles:
        print(f"name >>> '{role}'   id >>> '{role.id}'\n")

""" ikke tenk på denne :)
@client.command()  
@commands.is_owner()
async def hub_get_star(ctx):
    star = await hub.get_star()
    embed = disc.Embed(title = star["name"], color = 0xFF5733)
    embed.set_image(url = star["photo"])
    await ctx.send(embed = embed)
"""

client.run(os.environ.get('Discord-Api-Token')) # discord api token hidden using a .env file