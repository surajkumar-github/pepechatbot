from itertools import filterfalse
import discord
from discord.client import Client
from discord.ext import commands, tasks
import giphy_client
from giphy_client.rest import ApiException
import random
from random import choice
from discord.ext.commands.core import command
from discord.ext.commands import BucketType
import os
import httpx as requests
import json
import datetime


client = commands.Bot(command_prefix=['pepe ', 'Pepe ', 'PEPE '], case_insensitive=True)
client.remove_command('help')

status = ['pepe help', 'v2 comming soon']
queue = []

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `?help` command for details!')
        
@client.command(name='ping', help='**This command returns the latency**')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')

@client.command(name='hi', help='**The bot type a random welcome message**')
async def hi(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    async with ctx.typing():
        await ctx.send(choice(responses))   


@client.command(name='die', help='**This command returns a random last words**')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(choice(responses))

@client.command(name='credits', help='**This command returns the credits**')
async def credits(ctx):
    await ctx.send('Made by `Suraj`')
    
@client.command(name='creditz', help='**This command returns the TRUE credits**')
async def creditz(ctx):
    await ctx.send('**No one but me, lozer!**')
   
@client.command(name='bye', help='**The bot type a bye message**')
async def bye(ctx):
    responses = ['Chala ja Bsdk', 'Pehli phursat me nikal ', 'Cya :)', 'bye', 'nice to meet you , bye']
    async with ctx.typing():
        await ctx.send(choice(responses))   

@client.command(name='version', help='**The bot type a bots version**')
async def version(context):
    print('here')
    myEmbed = discord.Embed(title="Current Version", description="```The Bot is in Version 1.0```", colour=0x00ff00)
    myEmbed.add_field(name="Version Code", value="```v1.0.0```", inline=False)
    myEmbed.add_field(name="Date Released", value="```20th April 2021```", inline=False)
    myEmbed.set_footer(text="This Bot is created by SURAJ")
    await context.message.channel.send(embed=myEmbed)    

@client.command(name='dinosaur_fact', help='**random dinosaur facts**')
async def dinosaur_fact(ctx):
    responses = ['Dinosaurs are a group of reptiles that have lived on Earth for about 245 million years', 'In 1842, the English naturalist Sir Richard Owen coined the term Dinosauria, derived from the Greek deinos, meaning “fearfully great,” and sauros, meaning “lizard', 'Dinosaur fossils have been found on all seven continents', 'All non-avian dinosaurs went extinct about 66 million years ago', 'There are roughly 700 known species of extinct dinosaurs', 'Modern birds are a kind of dinosaur because they share a common ancestor with non-avian dinosaurs']
    async with ctx.typing():
        await ctx.send(choice(responses))   

@client.command(name='joke', help='**random jokes**')
async def joke(ctx):
    responses = ['https://media.discordapp.net/attachments/819534363728805918/834466102569467954/0eacbd797c15fb7bcc7d4a80c0ce84b0.png?width=437&height=436', 'https://media.discordapp.net/attachments/819534363728805918/834465387902664724/15935020215efae94530944.png?width=515&height=436', 'https://cdn.discordapp.com/attachments/819534363728805918/834469801879404584/7e871c31529b97e624a7fe5194e618f8.png', 'https://media.discordapp.net/attachments/819534363728805918/834469600892551189/1345553-scan0042.png?width=283&height=436', 'https://media.discordapp.net/attachments/819534363728805918/834470288069623838/rippedpants.png']
    async with ctx.typing():
        await ctx.send(choice(responses))

# image commands

@client.command(name='band', help='**pepe band gif**')
async def band(context):
    print('here')
    myEmbed = discord.Embed(title="You are using pepe band....", description="", colour=0x00ff00)
    myEmbed.set_image(url="https://images-ext-1.discordapp.net/external/BAT_QN4Sj_B97BmLiv7no162WN1rXfkJyTaBrx3JmRs/https/media.discordapp.net/attachments/798822305798160384/833441866997301268/image0-2.gif")
    await context.message.channel.send(embed=myEmbed)    

@client.command(name='puppy', help='**puppy gif**')
async def puppy(context):
    print('here')
    myEmbed = discord.Embed(title="OwO, a cute little puppy....", description="", colour=0x00ff00)
    myEmbed.set_image(url="https://cdn.discordapp.com/attachments/819534363728805918/834365523634421790/tenor_10.gif")
    await context.message.channel.send(embed=myEmbed)   

@client.command(name='cat', help='**cat gif**')
async def cat(context):
    print('here')
    myEmbed = discord.Embed(title="cute kitty....", description="", colour=0x00ff00)
    myEmbed.set_image(url="https://cdn.discordapp.com/attachments/819534363728805918/834367629249871872/tenor_11.gif")
    await context.message.channel.send(embed=myEmbed)

@client.command(name='bunny', help='**bunny gif**')
async def bunny(context):
    print('here')
    myEmbed = discord.Embed(title="snow's cute bunny....", description="", colour=0x00ff00)
    myEmbed.set_image(url="https://cdn.discordapp.com/attachments/819534363728805918/834379897484476426/tenor_13.gif")
    await context.message.channel.send(embed=myEmbed)  
# other commands

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@client.command() 
async def add(ctx,a:int,b:int): 
    await ctx.send(f"{a} + {b} = {a+b}") #Adds A and B

@client.command() 
async def sub(ctx,a:int,b:int): 
    await ctx.send(f"{a} - {b} = {a-b}") #Subtracts A and B

@client.command() 
async def mul(ctx,a:int,b:int): 
    await ctx.send(f"{a} * {b} = {a*b}") #Multplies A and B

@client.command() 
async def div(ctx,a:int,b:int): 
    await ctx.send(f"{a} / {b} = {a/b}") #Divides A and B
    
@client.command()
async def say(ctx, *, args):
    async with ctx.typing():
        await ctx.send(args)
        await ctx.message.delete()
    
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

@client.command()
async def membercount(ctx):
    embed = discord.Embed(colour=discord.Colour.orange())

    embed.set_author(name="Member Count", icon_url=ctx.guild.icon_url)
    embed.add_field(name="Total", value=ctx.guild.member_count)
    embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)


@client.command()
async def av(ctx, *, member: discord.Member = None):
    if not member:member=ctx.message.author

    message = discord.Embed(title=str(member), color=discord.Colour.red())
    message.set_image(url=member.avatar_url)

    await ctx.send(embed=message)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} has been banned.")

@client.command()
async def fact(ctx):
    start = "Did you know that "
    facts = ["Banging your head against a wall for one hour burns 150 calories.",
            "Snakes can help predict earthquakes.",
            "7% of American adults believe that chocolate milk comes from brown cows.",
            "If you lift a kangaroo’s tail off the ground it can’t hop.",
            "Bananas are curved because they grow towards the sun.",
            "Billy goats urinate on their own heads to smell more attractive to females.",
            "The inventor of the Frisbee was cremated and made into a Frisbee after he died.",
            "During your lifetime, you will produce enough saliva to fill two swimming pools.",
            "Polar bears could eat as many as 86 penguins in a single sitting…",
            "Heart attacks are more likely to happen on a Monday.",
            "In 2017 more people were killed from injuries caused by taking a selfie than by shark attacks.",
            "A lion’s roar can be heard from 5 miles away.",
            "The United States Navy has started using Xbox controllers for their periscopes.",
            "A sheep, a duck and a rooster were the first passengers in a hot air balloon.",
            "The average male gets bored of a shopping trip after 26 minutes.",
            "Recycling one glass jar saves enough energy to watch television for 3 hours.",
            "Approximately 10-20% of U.S. power outages are caused by squirrels."
        ]
    fact_file = open("facts.txt", mode="r", encoding="utf8")
    fact_file_facts = fact_file.read().split("\n")
    fact_file.close()

    for i in fact_file_facts:
        if i == "": fact_file_facts.remove(i)

    facts = facts + fact_file_facts

    await ctx.send(start + random.choice(facts).lower())

@client.command()
@commands.cooldown(1, 10, BucketType.user)
async def slap_member(ctx, member: discord.Member):
        apikey = os.environ["3BMUFLN4ST6C"]
        lmt = 20
        search_term = "slap"
        r = requests.get("https://api.tenor.com/v1/search?q={search_term}&key=${process.env.TENORKEY}&limit=20")

        if r.status_code == 200:  
            top_gifs = json.loads(r.content)
            uri = random.choice(random.choice(top_gifs['results'])['media'])["gif"]["url"]

        else:
            embed = discord.Embed(title=f"The site was unable to be reached. Please try again later", colour=discord.Colour.blurple())
            return await ctx.send(embed=embed)

        embed = discord.Embed(title = f"{ctx.author.display_name} slapped {member.display_name}!", colour=discord.Colour.blurple())

        embed.set_image(url=uri)
        embed.set_footer(text="Powered by Tenor")
        await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 10, BucketType.user)
async def hit_member(ctx, member: discord.Member):
        apikey = ["3BMUFLN4ST6C"]
        lmt = 20
        search_term = "punch"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            top_gifs = json.loads(r.content)
            uri = random.choice(random.choice(top_gifs['results'])['media'])["gif"]["url"]

        else:
            embed = discord.Embed(title=f"The site was unable to be reached. Please try again later", colour=discord.Colour.blurple())
            return await ctx.send(embed=embed)

        embed = discord.Embed(title=f"{ctx.author.display_name} punched {member.display_name}!", colour=discord.Colour.blurple())

        embed.set_image(url=uri)
        embed.set_footer(text="Powered by Tenor")
        await ctx.send(embed=embed)

@client.command()
async def gif(ctx,*,q="random"):

    api_key="yLoJwv5SZw53kwXy6luYUi6UE81C77PH"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command()
async def punch(ctx,*, member : discord.Member=None):

    api_key="yLoJwv5SZw53kwXy6luYUi6UE81C77PH"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        q="punch"
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=f"{ctx.author.display_name} punched {member.display_name}!", colour=discord.Colour.blurple())
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)        

@client.command()
async def slap(ctx,*, member : discord.Member=None):

    api_key="yLoJwv5SZw53kwXy6luYUi6UE81C77PH"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        q="slap"
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=f"{ctx.author.display_name} slapped {member.display_name}!", colour=discord.Colour.blurple())
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)          

@client.command()
async def kick(ctx,*, member : discord.Member=None):

    api_key="yLoJwv5SZw53kwXy6luYUi6UE81C77PH"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        q="kick"
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=f"{ctx.author.display_name} kicked {member.display_name}!", colour=discord.Colour.blurple())
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)  

@client.command()
async def hug(ctx,*, member : discord.Member=None):

    api_key="yLoJwv5SZw53kwXy6luYUi6UE81C77PH"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        q="anime hug"
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=f"{ctx.author.display_name} hugged {member.display_name}!", colour=discord.Colour.blurple())
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)  

client.run('ODMzNzMzMDgxMTQzMDUwMjkw.YH2ocA.I64_-wmBUzNAAKLm3M7ssxHgDuw')