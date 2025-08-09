import schedule
import requests
import os
import discord
import asyncio
import random
from discord.ext import commands
from discord.ext import tasks
from keep_alive import keep_alive
import datetime
import time

client = commands.Bot(command_prefix='--',intents=discord.Intents.default())

TOKEN=(os.getenv("TOKEN"))

MONDAY_TIMINGS='https://media.discordapp.net/attachments/818792417729052685/930323874606882826/unknown.png'
TUE_WED_THUR_TIMINGS='https://media.discordapp.net/attachments/818792417729052685/930323976452997180/unknown.png?width=350&height=406'
FRI_TIMINGS='https://media.discordapp.net/attachments/818792417729052685/930323855342444604/unknown.png?width=406&height=406'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="--hello"))
    client.loop.create_task(my_background_task())


#@client.event
#async def on_raw_reaction_add(payload):
#    channel = client.get_channel(payload.channel_id)
#    message = await channel.fetch_message(payload.message_id)
#    user = client.get_user(payload.user_id)
#    if payload.channel_id == 820357712478994482:
#        emoji = payload.emoji
#        await message.remove_reaction(emoji, user)
#        await channel.send("Please refrain from adding reactions here. No reaction allowed as a result of reactions spaming by few members",delete_after=20)

@client.command(aliases=['Hello','HELLO'])
async def hello(ctx):
    await ctx.message.delete()
    msg="Hello {0}".format(ctx.message.author.mention)
    await ctx.send(msg)


@client.command(aliases=['logout','Stop','STOP'])
async def stop(ctx):
  if ctx.message.author.id == 710359673194152008:
    await ctx.message.delete()
    msg="{0} Stopping Bot on command call".format(ctx.message.author.mention)
    await ctx.send(msg)
    await client.close()
  elif ctx.message.author.id == 625247146274193409:
    await ctx.message.delete()
    msg="{0} Stopping Bot on command call".format(ctx.message.author.mention)
    await ctx.send(msg)
    await client.close()
  else:
    await ctx.send("Sorry only <@625247146274193409> and <@710359673194152008> can use this command for obvious reasons")

@tasks.loop(seconds=1.0, count=1)
async def break0():
    await client.wait_until_ready()
    print(break0.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',color=random.randint(0, 16777215))

    embed.add_field(name='BREAK Period',
    value='<@&906262684163526696>:- 10-A:- BREAK ! \n<@&818827865478397982>:- 10-C:- BREAK !\n<@&889789088704634930>:- 10-D:- BREAK !\n<@&818828055698210857>:- 10-F:- BREAK !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    wat_day=datetime.datetime.today().weekday()

    if wat_day == 0:
        embed.set_thumbnail(url=MONDAY_TIMINGS)
    elif wat_day == 1:
        embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)
    elif wat_day == 2:
        embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)
    elif wat_day == 3:
        embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)
    elif wat_day == 4:
        embed.set_thumbnail(url=FRI_TIMINGS)

    await channel.send(embed=embed)


@break0.before_loop
async def before():
    await client.wait_until_ready()


def br():
    break0.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period00():
    await client.wait_until_ready()
    print(monday_period00.current_loop)
    channel = client.get_channel(820357712478994482)

    wat_day=datetime.datetime.today().weekday()
    print(wat_day)
    if wat_day == 0:
        url = "REDACTED"

        data = {
            "content" : ('<@&906262684163526696>'+'<@&818827865478397982>'+'<@&889789088704634930>'+'<@&818828055698210857>'),
            "username" : "Ping Bot v.2.0"
        },

        data["embeds"] = [
            {
            "title": "Period  Reminder :-",
            "description": "<@&906262684163526696> <@&818827865478397982> <@&889789088704634930> <@&818828055698210857> :-**``REGISTRATION PERIOD.``**\n\n`School Starting now.`\n\n``NOTE :- Let Nathan know if u want to add a specific link or anything for the bot :)``",
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "color": random.randint(0, 16777215),
            "image": {
                "url": "https://media.discordapp.net/attachments/818792417729052685/927768781839826994/Screen_Shot_2022-01-04_at_7.png"
            },
            "thumbnail": {
                "url": MONDAY_TIMINGS
            }
            },
            {
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "image": {
                "url": "https://media.discordapp.net/attachments/818792417729052685/881392700899856506/unknown_1.png?width=625&height=406"
            }
            },
            {
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "image": {
                "url": "https://media.discordapp.net/attachments/916268604553580585/931216891811356692/AD31851C-9BAF-4197-8FFC-B271AD8124F6.jpg?width=585&height=406"
            }
            },
            {
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "image": {
                "url": "https://media.discordapp.net/attachments/919900305183875104/930869166410461224/image0.jpg?width=515&height=406"
            }
            }
        ]

        result = requests.post(url, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

    elif wat_day == 4:
        url = "REDACTED" 

        data = {
            "content" : ('<@&906262684163526696>'+'<@&818827865478397982>'+'<@&889789088704634930>'+'<@&818828055698210857>'),
            "username" : "Ping Bot v.2.0"
        }

        data["embeds"] = [
            {
            "title": "Period  Reminder :-",
            "description": "<@&906262684163526696> <@&818827865478397982> <@&889789088704634930> <@&818828055698210857> :-**``REGISTRATION PERIOD.``**\n\n`School Starting now.`\n\n``NOTE :- Let Nathan know if u want to add a specific link or anything for the bot :)``",
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "color": random.randint(0, 16777215),
            "image": {
                "url": "https://media.discordapp.net/attachments/818792417729052685/927768781839826994/Screen_Shot_2022-01-04_at_7.png"
            },
            "thumbnail": {
                "url": FRI_TIMINGS
            }
            },
            {
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "image": {
                "url": "https://media.discordapp.net/attachments/818792417729052685/881392700899856506/unknown_1.png?width=625&height=406"
            }
            },
            {
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "image": {
                "url": "https://media.discordapp.net/attachments/916268604553580585/931216891811356692/AD31851C-9BAF-4197-8FFC-B271AD8124F6.jpg?width=585&height=406"
            }
            },
            {
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "image": {
                "url": "https://media.discordapp.net/attachments/919900305183875104/930869166410461224/image0.jpg?width=515&height=406"
            }
            }
        ]

        result = requests.post(url, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))
    
    else:
        url = "REDACTED"
        data = {
            "content" : ('<@&906262684163526696>'+'<@&818827865478397982>'+'<@&889789088704634930>'+'<@&818828055698210857>'),
            "username" : "Ping Bot v.2.0"
        }

        data["embeds"] = [
            {
            "title": "Period  Reminder :-",
            "description": "<@&906262684163526696> <@&818827865478397982> <@&889789088704634930> <@&818828055698210857> :-**``REGISTRATION PERIOD.``**\n\n`School Starting now.`\n\n``NOTE :- Let Nathan know if u want to add a specific link or anything for the bot :)``",
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "color": random.randint(0, 16777215),
            "image": {
                "url": "https://media.discordapp.net/attachments/818792417729052685/927768781839826994/Screen_Shot_2022-01-04_at_7.png"
            },
            "thumbnail": {
                "url": TUE_WED_THUR_TIMINGS
            }
            },
            {
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "image": {
                "url": "https://media.discordapp.net/attachments/818792417729052685/881392700899856506/unknown_1.png?width=625&height=406"
            }
            },
            {
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "image": {
                "url": "https://media.discordapp.net/attachments/916268604553580585/931216891811356692/AD31851C-9BAF-4197-8FFC-B271AD8124F6.jpg?width=585&height=406"
            }
            },
            {
            "url": "https://PING-BOT.nathanmoreas.repl.co",
            "image": {
                "url": "https://media.discordapp.net/attachments/919900305183875104/930869166410461224/image0.jpg?width=515&height=406"
            }
            }
        ]

        result = requests.post(url, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))

@monday_period00.before_loop
async def before():
    await client.wait_until_ready()


def s00():
    monday_period00.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period0():
    await client.wait_until_ready()
    print(monday_period0.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Monday 0th Period',
    value='<@&906262684163526696>:- 10-A:- CHEMISTRY / ECONOMICS PERIOD ! \n<@&818827865478397982>:- 10-C:- ARABIC PERIOD !\n<@&889789088704634930>:- 10-D:- CHEMISTRY / ECONOMICS PERIOD !\n<@&818828055698210857>:- 10-F:- MATHS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=MONDAY_TIMINGS)

    await channel.send(embed=embed)


@monday_period0.before_loop
async def before():
    await client.wait_until_ready()


def s0():
    monday_period0.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period1():
    await client.wait_until_ready()
    print(monday_period1.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Monday 1st Period',
    value='<@&906262684163526696>:- 10-A:- MATHS PERIOD ! \n<@&818827865478397982>:- 10-C:- ENGLISH LANGUAGE PERIOD !\n<@&889789088704634930>:- 10-D:- ARABIC PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER MATHS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=MONDAY_TIMINGS)

    await channel.send(embed=embed)


@monday_period1.before_loop
async def before():
    await client.wait_until_ready()


def s1():
    monday_period1.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period2():
    await client.wait_until_ready()
    print(monday_period2.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Monday 2nd Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER MATHS PERIOD ! \n<@&818827865478397982>:- 10-C:- ANOTHER ENGLISH LANGUAGE PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER ARABIC PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER MATHS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=MONDAY_TIMINGS)

    await channel.send(embed=embed)


@monday_period2.before_loop
async def before():
    await client.wait_until_ready()


def s2():
    monday_period2.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period3():
    await client.wait_until_ready()
    print(monday_period3.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Monday 3rd Period',
    value='<@&906262684163526696>:- 10-A:- BIO / ACC PERIOD ! \n<@&818827865478397982>:- 10-C:- CHEMISTRY / ECONOMICS PERIOD !\n<@&889789088704634930>:- 10-D:- BIO / ACC PERIOD !\n<@&818828055698210857>:- 10-F:- CHEMISTRY / ECONOMICS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=MONDAY_TIMINGS)

    await channel.send(embed=embed)


@monday_period3.before_loop
async def before():
    await client.wait_until_ready()


def s3():
    monday_period3.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period4():
    await client.wait_until_ready()
    print(monday_period4.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Monday 4th Period',
    value='<@&906262684163526696>:- 10-A:- ENG.LIT / ART / PSYCHO / HISTORY PERIOD ! \n<@&818827865478397982>:- 10-C:- ENG.LIT / ART / PSYCHO / HISTORY PERIOD !\n<@&889789088704634930>:- 10-D:- ENG.LIT / ART / PSYCHO / HISTORY PERIOD !\n<@&818828055698210857>:- 10-F:- ENG.LIT / ART / PSYCHO / HISTORY PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=MONDAY_TIMINGS)

    await channel.send(embed=embed)


@monday_period4.before_loop
async def before():
    await client.wait_until_ready()


def s4():
    monday_period4.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period5():
    await client.wait_until_ready()
    print(monday_period5.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Monday 5th Period',
    value='<@&906262684163526696>:- 10-A:- SPORTS PERIOD ! \n<@&818827865478397982>:- 10-C:- PYSHICS / BUSINESS PERIOD !\n<@&889789088704634930>:- 10-D:- ENGLISH LANGUAGE PERIOD !\n<@&818828055698210857>:- 10-F:- PYSHICS / BUSINESS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=MONDAY_TIMINGS)

    await channel.send(embed=embed)


@monday_period5.before_loop
async def before():
    await client.wait_until_ready()


def s5():
    monday_period5.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period6():
    await client.wait_until_ready()
    print(monday_period6.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Monday 6th Period',
    value='<@&906262684163526696>:- 10-A:- PYSHICS / BUSINESS PERIOD ! \n<@&818827865478397982>:- 10-C:- BIO / ACC PERIOD !\n<@&889789088704634930>:- 10-D:- PYSHICS / BUSINESS PERIOD !\n<@&818828055698210857>:- 10-F:- BIO / ACC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=MONDAY_TIMINGS)

    await channel.send(embed=embed)


@monday_period6.before_loop
async def before():
    await client.wait_until_ready()


def s6():
    monday_period6.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period7():
    await client.wait_until_ready()
    print(monday_period7.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Monday 7th Period',
    value='<@&906262684163526696>:- 10-A:- COMP SCI / ICT PERIOD ! \n<@&818827865478397982>:- 10-C:- ANOTHER BIO / ACC PERIOD !\n<@&889789088704634930>:- 10-D:- COMP SCI / ICT PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER BIO / ACC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=MONDAY_TIMINGS)

    await channel.send(embed=embed)


@monday_period7.before_loop
async def before():
    await client.wait_until_ready()


def s7():
    monday_period7.start()


@tasks.loop(seconds=1.0, count=1)
async def monday_period8():
    await client.wait_until_ready()
    print(monday_period8.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Monday 8th Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER COMP SCI / ICT PERIOD ! \n<@&818827865478397982>:- 10-C:- MATHS PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER COMP SCI / ICT PERIOD !\n<@&818828055698210857>:- 10-F:- ENGLISH LANGUAGE PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=MONDAY_TIMINGS)

    await channel.send(embed=embed)


@monday_period8.before_loop
async def before():
    await client.wait_until_ready()


def s8():
    monday_period8.start()


@tasks.loop(seconds=1.0, count=1)
async def tuesday_period1():
    await client.wait_until_ready()
    print(tuesday_period1.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Tuesday 1st Period',
    value='<@&906262684163526696>:- 10-A:- ARABIC PERIOD ! \n<@&818827865478397982>:- 10-C:- UAE SST PERIOD !\n<@&889789088704634930>:- 10-D:- MATHS PERIOD !\n<@&818828055698210857>:- 10-F:- MORAL ED PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@tuesday_period1.before_loop
async def before():
    await client.wait_until_ready()


def m1():
    tuesday_period1.start()


@tasks.loop(seconds=1.0, count=1)
async def tuesday_period2():
    await client.wait_until_ready()
    print(tuesday_period2.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Tuesday 2nd Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER ARABIC PERIOD ! \n<@&818827865478397982>:- 10-C:- CHEMISTRY / ECONOMICS PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER MATHS PERIOD !\n<@&818828055698210857>:- 10-F:- CHEMISTRY / ECONOMICS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@tuesday_period2.before_loop
async def before():
    await client.wait_until_ready()


def m2():
    tuesday_period2.start()


@tasks.loop(seconds=1.0, count=1)
async def tuesday_period3():
    await client.wait_until_ready()
    print(tuesday_period3.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Tuesday 3rd Period',
    value='<@&906262684163526696>:- 10-A:- ENGLISH LANGUAGE PERIOD ! \n<@&818827865478397982>:- 10-C:- ANOTHER CHEMISTRY / ECONOMICS PERIOD !\n<@&889789088704634930>:- 10-D:- UAE SST PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER CHEMISTRY / ECONOMICS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@tuesday_period3.before_loop
async def before():
    await client.wait_until_ready()


def m3():
    tuesday_period3.start()


@tasks.loop(seconds=1.0, count=1)
async def tuesday_period4():
    await client.wait_until_ready()
    print(tuesday_period4.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Tuesday 4th Period',
    value='<@&906262684163526696>:- 10-A:- CHEMISTRY / ECONOMICS PERIOD ! \n<@&818827865478397982>:- 10-C:- BIO / ACC PERIOD !\n<@&889789088704634930>:- 10-D:- CHEMISTRY / ECONOMICS PERIOD !\n<@&818828055698210857>:- 10-F:- BIO / ACC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@tuesday_period4.before_loop
async def before():
    await client.wait_until_ready()


def m4():
    tuesday_period4.start()


@tasks.loop(seconds=1.0, count=1)
async def tuesday_period5():
    await client.wait_until_ready()
    print(tuesday_period5.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Tuesday 5th Period',
    value='<@&906262684163526696>:- 10-A:- BIO /ACC PERIOD ! \n<@&818827865478397982>:- 10-C:- PYSHICS / BUSINESS PERIOD !\n<@&889789088704634930>:- 10-D:- BIO /ACC PERIOD !\n<@&818828055698210857>:- 10-F:- PYSHICS / BUSINESS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@tuesday_period5.before_loop
async def before():
    await client.wait_until_ready()


def m5():
    tuesday_period5.start()


@tasks.loop(seconds=1.0, count=1)
async def tuesday_period6():
    await client.wait_until_ready()
    print(tuesday_period6.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Tuesday 6th Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER BIO /ACC PERIOD ! \n<@&818827865478397982>:- 10-C:- ENGLISH LANGUAGE PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER BIO /ACC PERIOD !\n<@&818828055698210857>:- 10-F:- MATHS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@tuesday_period6.before_loop
async def before():
    await client.wait_until_ready()


def m6():
    tuesday_period6.start()


@tasks.loop(seconds=1.0, count=1)
async def tuesday_period7():
    await client.wait_until_ready()
    print(tuesday_period7.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Tuesday 7th Period',
    value='<@&906262684163526696>:- 10-A:- MORAL ED PERIOD ! \n<@&818827865478397982>:- 10-C:- ANOTHER ENGLISH LANGUAGE PERIOD !\n<@&889789088704634930>:- 10-D:- SPORTS PERIOD !\n<@&818828055698210857>:- 10-F:- ARABIC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@tuesday_period7.before_loop
async def before():
    await client.wait_until_ready()


def m7():
    tuesday_period7.start()


@tasks.loop(seconds=1.0, count=1)
async def tuesday_period8():
    await client.wait_until_ready()
    print(tuesday_period8.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Tuesday 8th Period',
    value='<@&906262684163526696>:- 10-A:- ENG.LIT / ART / PSYCHO / HISTORY PERIOD ! \n<@&818827865478397982>:- 10-C:- ENG.LIT / ART / PSYCHO / HISTORY PERIOD !\n<@&889789088704634930>:- 10-D:- ENG.LIT / ART / PSYCHO / HISTORY PERIOD !\n<@&818828055698210857>:- 10-F:- ENG.LIT / ART / PSYCHO / HISTORY PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@tuesday_period8.before_loop
async def before():
    await client.wait_until_ready()


def m8():
    tuesday_period8.start()


@tasks.loop(seconds=1.0, count=1)
async def wednesday_period1():
    await client.wait_until_ready()
    print(wednesday_period1.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Wednesday 1st Period',
    value='<@&906262684163526696>:- 10-A:- COMP SCI / ICT PERIOD !\n<@&818827865478397982>:- 10-C:- MATHS PERIOD !\n<@&889789088704634930>:- 10-D:- COMP SCI / ICT PERIOD !\n<@&818828055698210857>:- 10-F:- ENGLISH LANGUAGE PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@wednesday_period1.before_loop
async def before():
    await client.wait_until_ready()


def t1():
    wednesday_period1.start()


@tasks.loop(seconds=1.0, count=1)
async def wednesday_period2():
    await client.wait_until_ready()
    print(wednesday_period2.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Wednesday 2nd Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER COMP SCI / ICT PERIOD !\n<@&818827865478397982>:- 10-C:- PYSHICS / BUSINESS PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER COMP SCI / ICT PERIOD !\n<@&818828055698210857>:- 10-F:- PYSHICS / BUSINESS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)



@wednesday_period2.before_loop
async def before():
    await client.wait_until_ready()


def t2():
    wednesday_period2.start()


@tasks.loop(seconds=1.0, count=1)
async def wednesday_period3():
    await client.wait_until_ready()
    print(wednesday_period3.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Wednesday 3rd Period',
    value='<@&906262684163526696>:- 10-A:- MATHS PERIOD !\n<@&818827865478397982>:- 10-C:- ANOTHER PYSHICS / BUSINESS PERIOD ! \n<@&889789088704634930>:- 10-D:- MATHS PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER PYSHICS / BUSINESS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)

@wednesday_period3.before_loop
async def before():
    await client.wait_until_ready()


def t3():
    wednesday_period3.start()


@tasks.loop(seconds=1.0, count=1)
async def wednesday_period4():
    await client.wait_until_ready()
    print(wednesday_period4.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Wednesday 4th Period',
    value='<@&906262684163526696>:- 10-A:- 10-A:- ENGLISH LANGUAGE PERIOD !\n<@&818827865478397982>:- 10-C:- BIO / ACC PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER MATHS PERIOD !\n<@&818828055698210857>:- 10-F:- BIO / ACC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)
    

@wednesday_period4.before_loop
async def before():
    await client.wait_until_ready()


def t4():
    wednesday_period4.start()


@tasks.loop(seconds=1.0, count=1)
async def wednesday_period5():
    await client.wait_until_ready()
    print(wednesday_period5.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Wednesday 5th Period',
    value='<@&906262684163526696>:- 10-A:- CHEMISTRY / ECONOMICS PERIOD !\n<@&818827865478397982>:- 10-C:- COMP SCI / ICT PERIOD !\n<@&889789088704634930>:- 10-D:- CHEMISTRY / ECONOMICS PERIOD !\n<@&818828055698210857>:- 10-F:- COMP SCI / ICT PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)

@wednesday_period5.before_loop
async def before():
    await client.wait_until_ready()


def t5():
    wednesday_period5.start()


@tasks.loop(seconds=1.0, count=1)
async def wednesday_period6():
    await client.wait_until_ready()
    print(wednesday_period6.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Wednesday 6th Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER CHEMISTRY / ECONOMICS PERIOD !\n<@&818827865478397982>:- 10-C:- ANOTHER COMP SCI / ICT PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER CHEMISTRY / ECONOMICS PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER COMP SCI / ICT PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@wednesday_period6.before_loop
async def before():
    await client.wait_until_ready()


def t6():
    wednesday_period6.start()


@tasks.loop(seconds=1.0, count=1)
async def wednesday_period7():
    await client.wait_until_ready()
    print(wednesday_period7.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)

    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Wednesday 7th Period',
    value='<@&906262684163526696>:- 10-A:- ENG.LIT / ART / PSYCHO / HISTORY  PERIOD \n<@&818827865478397982>:- 10-C:- ENG.LIT / ART / PSYCHO / HISTORY  PERIOD !\n<@&889789088704634930>:- 10-D:- ENG.LIT / ART / PSYCHO / HISTORY  PERIOD !\n<@&818828055698210857>:- 10-F:- ENG.LIT / ART / PSYCHO / HISTORY  PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@wednesday_period7.before_loop
async def before():
    await client.wait_until_ready()


def t7():
    wednesday_period7.start()


@tasks.loop(seconds=1.0, count=1)
async def wednesday_period8():
    await client.wait_until_ready()
    print(wednesday_period8.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Wednesday 8th Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER ENG.LIT / ART / PSYCHO / HISTORY  PERIOD \n<@&818827865478397982>:- 10-C:- ANOTHER ENG.LIT / ART / PSYCHO / HISTORY  PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER ENG.LIT / ART / PSYCHO / HISTORY  PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER ENG.LIT / ART / PSYCHO / HISTORY  PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@wednesday_period8.before_loop
async def before():
    await client.wait_until_ready()


def t8():
    wednesday_period8.start()


@tasks.loop(seconds=1.0, count=1)
async def thursday_period1():
    await client.wait_until_ready()
    print(thursday_period1.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Thursday 1st Period',
    value='<@&906262684163526696>:- 10-A:- PYSHICS / BUSINESS PERIOD ! \n<@&818827865478397982>:- 10-C:- MATHS PERIOD !\n<@&889789088704634930>:- 10-D:- PYSHICS / BUSINESS PERIOD !\n<@&818828055698210857>:- 10-F:- ENGLISH LANGUAGE PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)
    

@thursday_period1.before_loop
async def before():
    await client.wait_until_ready()


def w1():
    thursday_period1.start()


@tasks.loop(seconds=1.0, count=1)
async def thursday_period2():
    await client.wait_until_ready()
    print(thursday_period2.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Thursday 2nd Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER PYSHICS / BUSINESS PERIOD ! \n<@&818827865478397982>:- 10-C:- ANOTHER MATHS PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER PYSHICS / BUSINESS PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER ENGLISH LANGUAGE PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@thursday_period2.before_loop
async def before():
    await client.wait_until_ready()


def w2():
    thursday_period2.start()


@tasks.loop(seconds=1.0, count=1)
async def thursday_period3():
    await client.wait_until_ready()
    print(thursday_period3.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Thursday 3rd Period',
    value='<@&906262684163526696>:- 10-A:- ARABIC PERIOD ! \n<@&818827865478397982>:- 10-C:- SPORTS PERIOD !\n<@&889789088704634930>:- 10-D:- ARABIC PERIOD !\n<@&818828055698210857>:- 10-F:- MATHS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@thursday_period3.before_loop
async def before():
    await client.wait_until_ready()


def w3():
    thursday_period3.start()


@tasks.loop(seconds=1.0, count=1)
async def thursday_period4():
    await client.wait_until_ready()
    print(thursday_period4.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Thursday 4th Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER ARABIC PERIOD ! \n<@&818827865478397982>:- 10-C:- ENGLISH LANGUAGE PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER ARABIC PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER MATHS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)



@thursday_period4.before_loop
async def before():
    await client.wait_until_ready()


def w4():
    thursday_period4.start()


@tasks.loop(seconds=1.0, count=1)
async def thursday_period5():
    await client.wait_until_ready()
    print(thursday_period5.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Thursday 5th Period',
    value='<@&906262684163526696>:- 10-A:- UAE SST PERIOD ! \n<@&818827865478397982>:- 10-C:- CHEMISTRY / ECONOMICS PERIOD !\n<@&889789088704634930>:- 10-D:- BIBLE PERIOD !\n<@&818828055698210857>:- 10-F:- CHEMISTRY / ECONOMICS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)



@thursday_period5.before_loop
async def before():
    await client.wait_until_ready()


def w5():
    thursday_period5.start()


@tasks.loop(seconds=1.0, count=1)
async def thursday_period6():
    await client.wait_until_ready()
    print(thursday_period6.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Thursday 6th Period',
    value='<@&906262684163526696>:- 10-A:- ENGLISH LANGUAGE PERIOD ! \n<@&818827865478397982>:- 10-C:- ARABIC PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER BIBLE PERIOD !\n<@&818828055698210857>:- 10-F:- SPORTS PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)



@thursday_period6.before_loop
async def before():
    await client.wait_until_ready()


def w6():
    thursday_period6.start()


@tasks.loop(seconds=1.0, count=1)
async def thursday_period7():
    await client.wait_until_ready()
    print(thursday_period7.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Thursday 7th Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER ENGLISH LANGUAGE PERIOD ! ! \n<@&818827865478397982>:- 10-C:- ANOTHER ARABIC PERIOD !\n<@&889789088704634930>:- 10-D:- ENGLISH LANGUAGE PERIOD !\n<@&818828055698210857>:- 10-F:- ARABIC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@thursday_period7.before_loop
async def before():
    await client.wait_until_ready()


def w7():
    thursday_period7.start()


@tasks.loop(seconds=1.0, count=1)
async def thursday_period8():
    await client.wait_until_ready()
    print(thursday_period8.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Thursday 8th Period',
    value='<@&906262684163526696>:- 10-A:- MATHS PERIOD ! \n<@&818827865478397982>:- 10-C:- MORAL ED PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER ENGLISH LANGUAGE PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER ARABIC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=TUE_WED_THUR_TIMINGS)

    await channel.send(embed=embed)


@thursday_period8.before_loop
async def before():
    await client.wait_until_ready()


def w8():
    thursday_period8.start()


@tasks.loop(seconds=1.0, count=1)
async def friday_period1():
    await client.wait_until_ready()
    print(friday_period1.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Friday 1st Period',
    value='<@&906262684163526696>:- 10-A:- MATHS PERIOD ! \n<@&818827865478397982>:- 10-C:- COMP SCI / ICT PERIOD !\n<@&889789088704634930>:- 10-D:- ENGLISH LANGUAGE PERIOD !\n<@&818828055698210857>:- 10-F:- COMP SCI / ICT PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=FRI_TIMINGS)

    await channel.send(embed=embed)


@friday_period1.before_loop
async def before():
    await client.wait_until_ready()


def th1():
    friday_period1.start()


@tasks.loop(seconds=1.0, count=1)
async def friday_period2():
    await client.wait_until_ready()
    print(friday_period2.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Friday 2nd Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER MATHS PERIOD ! \n<@&818827865478397982>:- 10-C:- ANOTHER COMP SCI / ICT PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER ENGLISH LANGUAGE PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER COMP SCI / ICT PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=FRI_TIMINGS)

    await channel.send(embed=embed)


@friday_period2.before_loop
async def before():
    await client.wait_until_ready()


def th2():
    friday_period2.start()


@tasks.loop(seconds=1.0, count=1)
async def friday_period3():
    await client.wait_until_ready()
    print(friday_period3.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Friday 3rd Period',
    value='<@&906262684163526696>:- 10-A:- ENGLISH LANGUAGE PERIOD ! \n<@&818827865478397982>:- 10-C:- BIBLE PERIOD !\n<@&889789088704634930>:- 10-D:- MORAL ED PERIOD !\n<@&818828055698210857>:- 10-F:- ARABIC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=FRI_TIMINGS)

    await channel.send(embed=embed)


@friday_period3.before_loop
async def before():
    await client.wait_until_ready()


def th3():
    friday_period3.start()


@tasks.loop(seconds=1.0, count=1)
async def friday_period4():
    await client.wait_until_ready()
    print(friday_period4.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Friday 4th Period',
    value='<@&906262684163526696>:- 10-A:- PYSHICS / BUSINESS PERIOD ! \n<@&818827865478397982>:- 10-C:- ANOTHER BIBLE PERIOD !\n<@&889789088704634930>:- 10-D:- PYSHICS / BUSINESS PERIOD !\n<@&818828055698210857>:- 10-F:- ENGLISH LANGUAGE PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=FRI_TIMINGS)

    await channel.send(embed=embed)


@friday_period4.before_loop
async def before():
    await client.wait_until_ready()


def th4():
    friday_period4.start()


@tasks.loop(seconds=1.0, count=1)
async def friday_period5():
    await client.wait_until_ready()
    print(friday_period5.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Friday 5th Period',
    value='<@&906262684163526696>:- 10-A:- BIO / ACC PERIOD ! \n<@&818827865478397982>:- 10-C:- MATHS PERIOD !\n<@&889789088704634930>:- 10-D:- BIO / ACC PERIOD !\n<@&818828055698210857>:- 10-F:- UAE SST PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=FRI_TIMINGS)

    await channel.send(embed=embed)


@friday_period5.before_loop
async def before():
    await client.wait_until_ready()


def th5():
    friday_period5.start()


@tasks.loop(seconds=1.0, count=1)
async def friday_period6():
    await client.wait_until_ready()
    print(friday_period6.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Friday 6th Period',
    value='<@&906262684163526696>:- 10-A:- BIBLE PERIOD ! \n<@&818827865478397982>:- 10-C:- ANOTHER MATHS PERIOD !\n<@&889789088704634930>:- 10-D:- MATHS PERIOD !\n<@&818828055698210857>:- 10-F:- BIBLE / ISLAMIC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=FRI_TIMINGS)

    await channel.send(embed=embed)


@friday_period6.before_loop
async def before():
    await client.wait_until_ready()


def th6():
    friday_period6.start()


@tasks.loop(seconds=1.0, count=1)
async def friday_period7():
    await client.wait_until_ready()
    print(friday_period7.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    embed = discord.Embed(title='Period Reminder :-',url='https://PING-BOT.nathanmoreas.repl.co',color=random.randint(0, 16777215))

    embed.add_field(name='Friday 7th Period',
    value='<@&906262684163526696>:- 10-A:- ANOTHER BIBLE PERIOD ! \n<@&818827865478397982>:- 10-C:- ARABIC PERIOD !\n<@&889789088704634930>:- 10-D:- ANOTHER MATHS PERIOD !\n<@&818828055698210857>:- 10-F:- ANOTHER BIBLE / ISLAMIC PERIOD !')
    
    embed.set_footer(text='Powered by Repl.it',icon_url=client.user.avatar_url)

    embed.timestamp = datetime.datetime.utcnow()

    embed.set_thumbnail(url=FRI_TIMINGS)

    await channel.send(embed=embed)


@friday_period7.before_loop
async def before():
    await client.wait_until_ready()


def th7():
    friday_period7.start()

@tasks.loop(seconds=1.0, count=1)
async def class_teacher():
    await client.wait_until_ready()
    print(class_teacher.current_loop)
    channel = client.get_channel(820357712478994482)
    msg = ('<@&906262684163526696>','<@&818827865478397982>','<@&889789088704634930>', '<@&818828055698210857>')
    await channel.send(msg)
    await channel.send("CLASS TEACHER MEETING / SESSION")
    


@class_teacher.before_loop
async def before():
    await client.wait_until_ready()


def clst():
    class_teacher.start()




@tasks.loop(seconds=1.0, count=1)
async def test():
    await client.wait_until_ready()
    print(test.current_loop)
    channel = client.get_channel(820357712478994482)
    wat_day=datetime.datetime.today().weekday()
    print(wat_day)
    channel_em = client.get_channel(930877220862459944)

    if wat_day == 0:
        em1 = await channel_em.fetch_message(930883140438859797)
        await channel.send(em1)
    elif wat_day == 1:
        em2 = await channel_em.fetch_message(930883809287753769)
        await channel.send(em2)
    elif wat_day == 2:
        em3 = await channel_em.fetch_message(930884075194032168)
        await channel.send(embed=em3.embeds[0])
    elif wat_day == 3:
        em4 = await channel_em.fetch_message(930884198007459850)
        await channel.send(embed=em4.embeds[0])
    elif wat_day == 4:
        em5 = await channel_em.fetch_message(930884361396551690)
        await channel.send(embed=em5.embeds[0])
    


@test.before_loop
async def before():
    await client.wait_until_ready()


def testt():
    test.start()

@client.event
async def my_background_task():
    await client.wait_until_ready()
    # these are in utc timezone timings also make sure ur doing use global and gmt +4
    schedule.every().monday.at("03:10").do(s00)
    schedule.every().monday.at("03:20").do(s0)
    schedule.every().monday.at("04:00").do(s1)
    schedule.every().monday.at("04:40").do(s2)
    schedule.every().monday.at("05:20").do(s3)
    schedule.every().monday.at("06:00").do(s4)
    schedule.every().monday.at("06:35").do(br)
    schedule.every().monday.at("06:55").do(s5)
    schedule.every().monday.at("07:35").do(s6)
    schedule.every().monday.at("08:10").do(s7)
    schedule.every().monday.at("08:50").do(s8)

    schedule.every().tuesday.at("03:10").do(s00)
    schedule.every().tuesday.at("03:30").do(m1)
    schedule.every().tuesday.at("04:10").do(m2)
    schedule.every().tuesday.at("04:50").do(m3)
    schedule.every().tuesday.at("05:30").do(m4)
    schedule.every().tuesday.at("06:10").do(br)
    schedule.every().tuesday.at("06:35").do(m5)
    schedule.every().tuesday.at("07:15").do(m6)
    schedule.every().tuesday.at("07:55").do(m7)
    schedule.every().tuesday.at("08:35").do(m8)

    schedule.every().wednesday.at("03:10").do(s00)
    schedule.every().wednesday.at("03:30").do(t1)
    schedule.every().wednesday.at("04:10").do(t2)
    schedule.every().wednesday.at("04:50").do(t3)
    schedule.every().wednesday.at("05:30").do(t4)
    schedule.every().wednesday.at("06:10").do(br)
    schedule.every().wednesday.at("06:35").do(t5)
    schedule.every().wednesday.at("07:15").do(t6)
    schedule.every().wednesday.at("07:55").do(t7)
    schedule.every().wednesday.at("08:35").do(t8)

    schedule.every().thursday.at("03:10").do(s00)
    schedule.every().thursday.at("03:30").do(w1)
    schedule.every().thursday.at("04:10").do(w2)
    schedule.every().thursday.at("04:50").do(w3)
    schedule.every().thursday.at("05:30").do(w4)
    schedule.every().thursday.at("06:10").do(br)
    schedule.every().thursday.at("06:35").do(w5)
    schedule.every().thursday.at("07:15").do(w6)
    schedule.every().thursday.at("07:55").do(w7)
    schedule.every().thursday.at("08:35").do(w8)

    schedule.every().friday.at("03:10").do(s00)
    schedule.every().friday.at("03:20").do(th1)
    schedule.every().friday.at("03:55").do(th2)
    schedule.every().friday.at("04:35").do(th3)
    schedule.every().friday.at("05:10").do(th4)
    schedule.every().friday.at("05:50").do(br)
    schedule.every().friday.at("06:10").do(th5)
    schedule.every().friday.at("06:45").do(th6)
    schedule.every().friday.at("07:20").do(th7)

    #schedule.every(6).seconds.do(s00)

    print("before while loop")
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        schedule.run_pending()
        await asyncio.sleep(1)


keep_alive()
client.run(TOKEN)