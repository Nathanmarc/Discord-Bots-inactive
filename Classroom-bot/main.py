import discord
import random
import os
import datetime
import asyncio
import aiohttp
import json
import requests
from serpapi import GoogleSearch
from dotenv import load_dotenv
from urllib.request import urlopen, Request
from discord.ext import commands
from discord.ext.commands import cog ,BucketType
from discord.ext import tasks
from os import environ
from bot_utils import imgfun
from bot_utils import *
from discord.utils import get
from discord.ext.commands import (CommandOnCooldown)
from bs4 import BeautifulSoup
from discord import HTTPException
from keep_alive import keep_alive
#from discord.utils import get
from anibotcommands.searchAnime import animeSearch
from anibotcommands.searchManga import mangaSearch
from anibotcommands.searchStudio import studioSearch
from anibotcommands.searchStaff import staffSearch
from anibotcommands.searchCharacter import charSearch

checkk = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(checkk.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

with open('config.json', 'r') as json_file:
  config = json.load(json_file)

# Feeling cute, might refactor later
MUTE_VOTE_TIME = config["MUTE_VOTE_TIME"]
MIN_MUTE_VOTERS = config["MIN_MUTE_VOTERS"] # should be 3
MUTE_TIME = config["MUTE_TIME"] # 10 mins

STATUS_LOOP = config["STATUS_LOOP"]

bot = commands.Bot(command_prefix='>>',intents=discord.Intents.default())
bot.remove_command('help')

# To store users who are currently being voted on
muted_users = []
muting_users = []

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

TOKEN=(os.getenv("TOKEN"))
IMAGE=(os.getenv("IMAGE"))
WEATHER=(os.getenv("WEATHER"))

def searchhimage(title):
  params = {
    "q": title,
    "tbm": "isch",
    "ijn": "0",
    "api_key": IMAGE
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  images_results = results['images_results']
  e=(images_results[0])
  urls = [e.get('thumbnail') for r in e]
  return(urls[0])


def question():
  url = "https://www.conversationstarters.com/generator.php"

  blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'text',
    'paragraph',
    'style',
    'link',
    'horizontal ruler',
    'border',
    'header',
    'center'

    ]

  try:
    page = urlopen(url)
  except:
    print("Error opening the URL")

  soup = BeautifulSoup(page, 'html.parser')

  content = soup.find('div', {"id": "random"})


  for t in content:
    if t.parent.name not in blacklist:
      content = '{} '.format(t)

  return (content)

async def status_loop():
    while True:
        await bot.change_presence(activity=discord.Game(name='{} servers | >>help | Bot made by Nathan'.format(len(bot.guilds))))
        await asyncio.sleep(STATUS_LOOP)

@bot.event
async def on_ready():
    print("Bot started.")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("--------------------------")

    await asyncio.sleep(10)
    bot.loop.create_task(status_loop())

@bot.event
async def on_member_join(member):
   channel=bot.get_channel(818796976094052373)
   await channel.send("https://media.discordapp.net/attachments/818796976094052373/934502167543422976/unknown.png")

@bot.command()
async def tst(ctx):
    await ctx.send(
    'Pick your roles',
    components = [
      Select(placeholder = 'Pick your Roles',
      options = [ 
        SelectOption(label="Biology",value="value1"),
        SelectOption(label="Chemistry",value="value2"),
        SelectOption(label="Physics",value="value3"),
        SelectOption(label="Accounts",value="value4"),
        SelectOption(label="Business",value="value5"),
        SelectOption(label="Economics",value="value6"),
        SelectOption(label="ICT",value="value7"),
        SelectOption(label="Computer Science",value="value8")
            ])])

@bot.event
async def on_select_option(interaction):
    if interaction.values[0] == "Biology":
      member = interaction.author
      role = discord.utils.get(interaction.server.roles, name="Biology")
      await bot.add_roles(member.author.id, role)
      await interaction.channel.send("added role !")



@bot.group(aliases=['manual', 'commands', 'info','HELP'],invoke_without_command = True) # for this main command (.help)
async def help(ctx):
    embed = discord.Embed(title="Help |Usage & Other Info",colour=discord.Colour.orange())

    embed.add_field(inline=False,
        name="`>>help Images`",
        value="Display Pictures of people. e.g:>>cable"
    )

    embed.add_field(inline=False,
        name="`>>help Utility`",
        value="Useful Commands. e.g:>>mute , >>books , >>recommend"
    )

    embed.add_field(inline=False,
        name="`>>help Search`",
        value="Search commands. e.g:>>anime , >>wiki "
    )

    embed.add_field(inline=False,
        name="`>>help Fun`",
        value="Fun and few Bot usage commands. e.g:>>ud , >>urmom , >>hello , >>ping"
    )

    embed.add_field(inline=False,
        name="`>>help Random`",
        value="Random commands. e.g:>>dog , >>questions"
    )

    await ctx.send(embed=embed,delete_after=25)

@help.command(aliases=['utility'])   #For this command (.help Moderation)
async def Utility(ctx):
    embed = discord.Embed(title="Help | Utility Commands",colour=discord.Colour.orange())
    
    embed.add_field(inline=False,
        name="`>>mute` <user>",
        value=
            """Vote to mute user for {0} minutes.
            Vote time: {1} minutes
            Minimum Voters: {2}
            """.format(int(MUTE_TIME/60), int(MUTE_VOTE_TIME/60), MIN_MUTE_VOTERS)
    )

    embed.add_field(inline=False,
        name="`>>ping`",
        value="Get bot latency."
    )

    embed.add_field(inline=False,
        name="`>>weather <city>`",
        value="Get <city> weather details."
    )

    embed.add_field(inline=False,
        name="`>>recommend`",
        value="recommend a show / movie"
    )
    '''
    embed.add_field(inline=False,
        name="`>>timetable`",
        value="Exam Timetalbe"
    )'''

    embed.add_field(name= '`>>textbooks`', value="Embed page with textbook links will show", inline=False
    )

    embed.add_field(name= '`>>ans`', value="Embed page with textbook answers links will show", inline=False
    )

    await ctx.send(embed=embed,delete_after=60)

@help.command(aliases=['search'])
async def Search(ctx):
    embed = discord.Embed(title="Help | Search Commands",colour=discord.Colour.orange())

    embed.add_field(inline=False,
        name="`>>wiki`",
        value="search anything on wikipedia"
    )

    embed.add_field(inline=False,
        name="`>>lyrics <artist> , <name of song>`",
        value="Search lyrics of any song [COMMA IS IMPORTANT]"
    )
    
    embed.add_field(name= '`>>anime` <title>', value="Search anime by title or ID.", inline=False
    )
    
    embed.add_field(name= '`>>manga` <title>', value="Search manga by title or ID.", inline=False
    )

    embed.add_field(name= '`>>studio` <studio name>', value="Search a studio by their name.", inline=False
    )

    embed.add_field(name= '`>>staff` <staff name>', value="Search an actor by their name.", inline=False
    )

    embed.add_field(name= '`>>char` <character name>', value="Search a character by their name.", inline=False
    )

    await ctx.send(embed=embed,delete_after=60)
    
@help.command(aliases=['random'])
async def Random(ctx):
    embed = discord.Embed(title="Help | Random Commands",colour=discord.Colour.orange())

    embed.add_field(inline=False,
        name="`>>shibe`",
        value="Random dog :dog: :eyes:"
    )

    embed.add_field(inline=False,
        name="`>>cat`",
        value="Random cat :cat: :cat2:"
    )

    embed.add_field(inline=False,
        name="`>>bird`",
        value="Random birb :bird: :hatching_chick:"
    )

    embed.add_field(inline=False,
        name="`>>questions`",
        value="<not so infinite random question>"
    )

    await ctx.send(embed=embed,delete_after=60)

@help.command(aliases=['fun'])
async def Fun(ctx):
    embed = discord.Embed(title="Help | Fun and Bot Usage Commands",colour=discord.Colour.orange())

    embed.add_field(inline=False,
        name="`>>hello`",
        value="Hello <user>."
    )

    embed.add_field(inline=False,
        name="`>>me`",
        value="<user> is Cool!"
    )

    embed.add_field(inline=False,
        name="`>>urmom`",
        value="ur mom will be shown"
    )

    embed.add_field(inline=False,
        name="`>>mori`",
        value="Mori will be shown"
    )

    embed.add_field(inline=False,
        name="`>>ud`",
        value="Fun search dictionary"
    )

    await ctx.send(embed=embed,delete_after=60)

@bot.command(aliases=['Txtbkans','ans','ANS','BOOKSANS'])
async def textbooks_ans(ctx):
    await ctx.message.delete()

    embedd = discord.Embed(title="Textbook Answers",colour=discord.Colour.purple())

    embedd.add_field(name= 'Edexcel GCSE (9-1) Biology Answers', value="[Check it out.](https://www.dropbox.com/s/81h0z8wts3jaer1/BIOLOGY%20Edexcel%20%289-1%29%20Student%20book%20answers.pdf?dl=0)", inline=False
    )
    embedd.add_field(name= 'Edexcel GCSE (9-1) Chemistry Answers', value="[Check it out.](https://www.dropbox.com/s/qimtf5gzoq9211t/CHEMISTRY%20Edexcel%20%289-1%29%20Student%20book%20answers.pdf?dl=0)", inline=False
    )
    embedd.add_field(name= 'Edexcel GCSE (9-1) Physics Answers', value="[Check it out.](https://www.dropbox.com/s/13sxw5waenrhmm9/PHYSICS%20edgcse_ss_phys_sb_aap_answers.pdf?dl=0)", inline=False
    )
    embedd.add_field(name= 'Edexcel GCSE (9-1) Psychology', value="[Check it out.](https://mega.nz/file/D64zgC6a#z78EbJXvgqkalDjV6KmG1mf8uiZ9EV4q3sH9UXqT_9c)", inline=False
    )
    embedd.add_field(name= 'International Edexcel GCSE (9-1) Computer Science', value="[Check it out.](https://mega.nz/file/y2g2HQ7B#xRNHrD69lWk3xfsSGXMj5KyqovcVDzuCMBNtzhvywng)", inline=False
    )
    embedd.add_field(name="**NOTE :- YOU WILL NEED TO BE PATIENT AND WAIT FOR THE PDF OPTION TO SHOW AND FOR SOME BOOKS WITH A LOT OF PAGES YOU WILL NEED TO WAIT A WHILE FOR THE BOOK AND PAGES TO SHOW IN THE PDF VIEWER.**",value=':warning::warning::warning:', inline=False
    )
    
    embedd.set_footer(text='Powered by mega.nz\nThis message will be deleted automatically after 60 seconds')
    
    await ctx.send(embed=embedd)

@bot.command(aliases=['Textbooks','TEXTBOOKS','Books','books','BOOKS','book','BOOK','textbooks'])
async def command_textbooks(ctx):
    await ctx.message.delete()

    embedd = discord.Embed(title="Textbooks",colour=discord.Colour.purple())

    embedd.add_field(name= 'Edexcel GCSE (9-1) Biology', value="[Check it out.](https://mega.nz/file/fjBRRKAa#XsvqgWaR-EFw45_iDNeJpXOkUVrFii7o5HVQ_fJZXWI)", inline=False
    )
    embedd.add_field(name= 'Edexcel GCSE (9-1) Chemistry', value="[Check it out.](https://mega.nz/file/PvInmQrD#iNwsRsYekwP5b7lKSFNfDixB7l3p1LQSg5TJymPlalk)", inline=False
    )
    embedd.add_field(name= 'Edexcel GCSE (9-1) Physics', value="[Check it out.](https://mega.nz/file/jzYmHD7D#CB24w3kvPZ7eLdbbRG_CIXpaYuD9-fmbIodOqe1mUFs)", inline=False
    )
    embedd.add_field(name= 'Edexcel GCSE (9-1) Psychology', value="[Check it out.](https://mega.nz/file/6jZxVCiD#TPr8VCeinml05fqPqHStm5t5cLSShzQ4ix5U4I2-PaM)", inline=False
    )
    embedd.add_field(name= 'Edexcel International GCSE (9-1) Business', value="[Check it out.](https://mega.nz/file/26xWkbCS#FyNuvJk0aoLZJP0n_5PR4LQArllBqz2nrmFqo20vhS0)", inline=False
    )
    embedd.add_field(name= 'Edexcel International GCSE (9-1) Economics', value="[Check it out.](https://mega.nz/file/arpiQbSI#6Dx81-vwDYHbsRRh9fFF391VuhWu0wYa8tlWJNYa4DU)", inline=False
    )
    embedd.add_field(name= 'Edexcel International GCSE (9-1) Accounting', value="[Check it out.](https://mega.nz/file/SjgmhRxA#Jw0kurf4qjVnpV1wjuDBBnexmt-x4SuG1VNWlpvz-Ig)", inline=False
    )
    embedd.add_field(name= 'Edexcel GCSE (9-1) Mathematics', value="[Check it out.](https://mega.nz/file/qjJCibyA#_Uoub384r4BSOHtvuvnq_riVjhb_8pDTeacDD0kIq1g)", inline=False
    )
    embedd.add_field(name= 'Edexcel GCSE Computer Science (9-1) Student Book', value="[Check it out.](https://mega.nz/file/GroUnJRa#aA9Ra20oNOMN1vjmgxHL7sQsK7UmLk9Xz-Cr6mVLa7k)", inline=False
    )
    embedd.add_field(name= 'Edexcel GCSE (9-1) ICT', value="[Check it out.](https://mega.nz/file/y7AUVDpA#EE0nAd2BJ0Bxe_3xFMoSXLX5N68z4TFeIMiHHAs_UCU)", inline=False
    )
    embedd.add_field(name= 'The Strange Case of Dr. Jekyll and Mr. Hyde And Other Tales of Terror', value="[Check it out.](https://mega.nz/file/7yAGSTYb#bnMbbV3a6GPY0XZiH-Br4FP-7n1_wr7ss3ysaa6EKIU)", inline=False
    )
    embedd.add_field(name= 'Macbeth by Shakespeare, William', value="[Check it out.](https://mega.nz/file/miRhmSAD#y1tZam90o4UR25aeZGXvnRo1hwLW_5thO_pRAvHbSno)", inline=False
    )
    embedd.add_field(name= 'An Inspector Calls and Other Plays', value="[Check it out.](https://mega.nz/file/nuQTXCTC#-SFVLbpHIZ6KJb1aaaUY1DszVhQpZszFsl3CB_Zvjao)", inline=False
    )
    embedd.add_field(name="**NOTE :- YOU WILL NEED TO BE PATIENT AND WAIT FOR THE PDF OPTION TO SHOW AND FOR SOME BOOKS WITH A LOT OF PAGES YOU WILL NEED TO WAIT 1-5 MINUTES FOR THE BOOK AND PAGES TO SHOW IN THE PDF VIEWER.**",value=':warning::warning::warning:', inline=False
    )
    
    embedd.set_footer(text='Powered by mega.nz\nThis message will automatically be deleted after 60 seconds')
    
    await ctx.send(embed=embedd,delete_after=60)

@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == ">>hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hey dirtbag")


@bot.command(aliases=['Hello','hello','HELLO'])
async def command_hello(ctx):
    await ctx.message.delete()
    msg="Hello {0}".format(ctx.message.author.mention)
    await ctx.send(msg)

@bot.command(aliases=['Questions'])
async def questions (ctx):
    await ctx.message.delete()
    msg = question()
    await ctx.send(msg)

@bot.command(aliases=['Me','ME'])
async def me(ctx):
    await ctx.message.delete()
    msg="{0}, is Cool!".format(ctx.message.author.mention)
    await ctx.send(msg)

@bot.command(aliases=["shibe"])
async def dog (ctx):
    await ctx.message.delete()
    with urlopen(Request(url="http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true", headers={'User-Agent': 'Mozilla/5.0'})) as json_return:
        shibe_contents = json_return.read()
        msg="{0}, here is your random shibe:".format(ctx.message.author.name)
        url=json.loads(shibe_contents)[0]
    await ctx.send(embed=imgfun(msg, url),delete_after=60)

@bot.command(aliases=['bird'])
async def birb(ctx):
    await ctx.message.delete()
    with urlopen(Request(url="http://random.birb.pw/tweet.json", headers={'User-Agent': 'Mozilla/5.0'})) as json_return:
        # get image filename
        birb_contents = json_return.read()
        msg="{0}, here is your random birb:".format(ctx.message.author.name)
        # insert image filename into URL
        url="http://random.birb.pw/img/{}".format(json.loads(birb_contents)["file"])
    await ctx.send(embed=imgfun(msg, url),delete_after=60)

@bot.command(aliases=['kitty', 'kitti'])
async def cat(ctx):
    await ctx.message.delete()
    with urlopen(Request(url="http://aws.random.cat/meow", headers={'User-Agent': 'Mozilla/5.0'})) as json_return:
        # get image filename
        cat_contents = json_return.read()
        msg="{0}, here is your random cat:".format(ctx.message.author.name)
        # insert image filename into URL
        url=json.loads(cat_contents)["file"]
    await ctx.send(embed=imgfun(msg, url),delete_after=60)
    
@bot.command(aliases=['latency'])
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send("`Bot latency: {}s`".format(round(bot.latency, 2)),delete_after=30)

@bot.command()
async def mori(ctx):
  await ctx.message.delete()
  msg="{0}, Mori:".format(ctx.message.author.name)
  url=["https://media.tenor.com/images/1db06935ce8a55e1ef50061efe4bfe97/tenor.gif","https://media.tenor.com/images/b8aa951fd61985378ed075ca94c3eba3/tenor.gif","https://media.tenor.com/images/5316a1bfc56d0bf763380b9196ad42f1/tenor.gif","https://media.tenor.com/images/367bbf9f5a5edd59af9f6ca1e41d0068/tenor.gif","https://lh3.googleusercontent.com/_xDWsMKGKIYhLsUtxKeCTxBxgQx0TK18fXGNllwXhKY-TmvRTr4yrv2xCzuPx9_-YWmU=s85","https://lh3.googleusercontent.com/yly9ngpRDyhWoJNPJjfh_1zhomyIT2gvVAN_Qr45tll5HhoktatWZ3yLk_HCXU2tiZHqIA=s85","https://lh3.googleusercontent.com/X4_Lvdby3SI_e7olhM5ll6xPqaY-7jN_uxn22pd6ThxfqHUIIIMH6u4r2KkqWyQo-1qF_w=s85","https://lh3.googleusercontent.com/uCslFfHlV0LEFud397njxriKIGuuLoYkcYxs9qB7vabRP8cv1Z-h54t9hinhTrh_epgf=s111"]
  do=(random.choice(url))
  await ctx.send(embed=imgfun(msg,do),delete_after=60)

@bot.command()
async def urmom(ctx):
  await ctx.message.delete()
  msg="{0}, Ur mom:".format(ctx.message.author.name)
  url="https://www.mypokecard.com/my/galery/3iVVM9mbUNgl.jpg"
  await ctx.send(embed=imgfun(msg,url),delete_after=30)

@bot.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def mute(ctx, target_user:discord.User):
    await ctx.message.delete()

    if target_user in muting_users:
        await ctx.send("There is already a mute vote on `{}`!".format(target_user),delete_after=30)
        return
    elif target_user in muted_users:
        await ctx.send("`{}` is already muted!".format(target_user),delete_after=30)
        return
    elif (target_user.id == 8382676623834480759):
        await ctx.send("{} `Hey wth i thought we were friends u cant mute me illegal`".format(ctx.message.author.mention),delete_after=30)
        return
    elif (target_user.id == 8130596767943884819):
        await error_admin_targeted(ctx)
        await ctx.send("{} `Bastard Stoopid u CANNOT mute GOD, now go read the bible`".format(ctx.message.author.mention),delete_after=30)
        return
    elif (target_user.id == 7103596731941520089):
        await error_admin_targeted(ctx)
        await ctx.send("{} `Bastard he's the law ,u can't mute the Law`".format(ctx.message.author.mention),delete_after=30)
        return

    muting_users.append(target_user)
    member = ctx.message.author
    vote_passed = await take_vote(ctx, "Mute `{}`?\n⚠ NOTE: Can't mute users with an equal or higher role.".format(target_user), MUTE_VOTE_TIME, MIN_MUTE_VOTERS)
    muting_users.remove(target_user)

    if vote_passed:
        try:
          role = discord.utils.get(ctx.guild.roles, name="Muted")
          await target_user.add_roles(role)
          await ctx.send("**{0}, the majority has ruled that you should be muted.** See ya in {1} minutes!".format(target_user, int(MUTE_TIME/60)))
          await asyncio.sleep(MUTE_TIME)
          await target_user.remove_roles(role)
          await ctx.send("**{0}**,unmuted".format(target_user),delete_after=30)
          
            
        except discord.ext.commands.errors.CommandInvokeError:
          await error_admin_targeted(ctx)
          muted_users.remove(target_user)

@bot.command(aliases=['wolframalpha', 'wa','wac'])
async def oracle(ctx, *args):
    """
    Answers questions and queries using WolframAlpha's Simple API
    """

    query = '+'.join(args)
    url = f"https://api.wolframalpha.com/v1/result?appid={os.getenv('WOLFRAM_ALPHA_API_KEY')}&i={query}%3F"
    response = requests.get(url)

    if response.status_code == 501:
        await ctx.send("Unable to process that query")
        return

    await ctx.send(response.text)

@bot.command()
async def test(ctx, target_user:discord.User):
    await ctx.message.delete()
    await require_lower_permissions(ctx, target_user, bot)
    await ctx.send("success",delete_after=30)

@bot.command(aliases=["ANIME", "a"])
async def anime(ctx, *, title):
    embed = animeSearch(title)
    await ctx.send(embed=embed)


@bot.command(aliases=["MANGA", "m"])
async def manga(ctx, *, title):
    embed = mangaSearch(title)
    await ctx.send(embed=embed)


@bot.command(aliases=['STUDIO', 's'])
async def studio(ctx, *, studioName):
    embed = studioSearch(studioName)
    await ctx.send(embed=embed)


@bot.command(aliases=['STAFF', 'st'])
async def staff(ctx, *, staffName):
    embed = staffSearch(staffName)
    await ctx.send(embed=embed)


@bot.command(aliases=["CHARACTER", 'ch', 'char'])
async def character(ctx, *, charName):
    embed = charSearch(charName)
    await ctx.send(embed=embed)

@bot.command(aliases=['Recommend','Rec','rec'],pass_context=True)
async def recommend(ctx):
  def check(m):
        return m.author == ctx.author
  await ctx.message.delete()

  await ctx.send("**Check your Dm's!**",delete_after=30)

  await ctx.author.send("**The title of the media ?**")   
  msg = await bot.wait_for("message",check=check)

  await ctx.author.send("**Please provide some description as to why someone else might enjoy it**")
  msg1 = await bot.wait_for("message",check=check)

  await ctx.author.send("**Number of episodes (If a series) or else Imdb Title**")
  msg2 = await bot.wait_for("message",check=check)

  await ctx.author.send("**Picture (If ur sending no image please send random message in chat,an automatic image will found by the web please be aware it may be not accurate)**")
  msg3 = await bot.wait_for("message",check=check)

  embed = discord.Embed(title='Recommendation:', color=random.randint(0, 16777215))

  embed.add_field(name= '**Title:-**', 
  value=msg.content, inline=False)

  embed.add_field(name= '**Description:-**', 
  value=msg1.content, inline=False)

  embed.add_field(name= '**Episodes / Imdb Title:-**', 
  value=msg2.content, inline=False)

  attachments = msg3.attachments

  if len(attachments) > 0:
    embed.set_thumbnail(url=attachments[0].url)
  else:
    smart = (searchhimage(msg.content))
    embed.set_thumbnail(url=smart)

  embed.set_footer(text=f"Submitted by {ctx.author.name}.",icon_url=ctx.author.avatar_url)

  embed.timestamp = datetime.datetime.utcnow()

  channel = bot.get_channel(920644774350974997)

  sent_message = await channel.send(embed=embed)

  await sent_message.add_reaction("🟩")
  await sent_message.add_reaction("🟨")
  await sent_message.add_reaction("🟥")


@bot.command()
async def weather(ctx, *, city: str):
    api_key = WEATHER
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
      async with channel.typing():
          y = x["main"]
          current_temperature = y["temp"]
          current_temperature_celsiuis = str(round(current_temperature - 273.15))
          current_pressure = y["pressure"]
          current_humidity = y["humidity"]
          z = x["weather"]
          get_city_name = x["name"]
          weather_description = z[0]["description"]
          embed = discord.Embed(title=f"Weather in {get_city_name}",
          color=ctx.guild.me.top_role.color,
          timestamp=ctx.message.created_at,)
          embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
          embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
          embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
          embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
          embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
          embed.set_footer(text=f"Requested by {ctx.author.name}")
          await channel.send(embed=embed)
    else:
        await channel.send("City not found.")


@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('This command is on a %.2fs cooldown' % error.retry_after,delete_after=30)
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments.",delete_after=30)
    if isinstance(error, commands.CommandNotFound):
        await error_invalid_usage(ctx)
        print("Command not found.")
    else:
        await ctx.send("An Error occured",delete_after=30)
        print(error)

keep_alive()
bot.run(TOKEN)