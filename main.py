import discord
from discord.ext import commands, tasks

from random import choice

client = commands.Bot(command_prefix='pepe ')

status = ['pepe help', 'Learning!', 'Eating!', 'Sleeping!']
queue = []

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

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

client.run('ODMzNzMzMDgxMTQzMDUwMjkw.YH2ocA.I64_-wmBUzNAAKLm3M7ssxHgDuw')