import discord
import random
from discord.ext import commands
import urbandictionary as ud
import datetime
import pytz
import wikipedia
import typing as t
import aiohttp
import inspect
import lxml
import requests
import json
import os
import datetime as dt
from aiohttp import ClientSession

bot = commands.Bot(command_prefix = '>>')
LYRICS_URL = "https://some-random-api.ml/lyrics?title="

RAPID = (os.getenv("RAPID"))


class Utility(commands.Cog):
    '''Useful and utility commands.'''

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Utility Cog has been loaded\n-----")
      
    @commands.command(name="lyrics")
    async def lyrics_command(self, ctx,*,query: t.Optional[str]):
        name = query 
        print(name)

        async with ctx.typing():
            async with aiohttp.request("GET", LYRICS_URL + name, headers={}) as r:
                if not 200 <= r.status <= 299:
                    await ctx.send("No Lyrics Found")

                data = await r.json()

                if len(data["lyrics"]) > 2000:
                    return await ctx.send(f"<{data['links']['genius']}>")

                embed = discord.Embed(
                    title=data["title"],
                    description=data["lyrics"],
                    colour=random.randint(0, 16777215),
                    timestamp=dt.datetime.utcnow(),
                )
                embed.set_thumbnail(url=data["thumbnail"]["genius"])
                embed.set_author(name=data["author"],icon_url=data["thumbnail"]["genius"])
                embed.set_footer(text=f"Called by / For {ctx.author.name}.\nPowered by Genius.",icon_url=ctx.author.avatar_url)

                await ctx.send(embed=embed)

    @commands.command(aliases=['wikipedia','search'])
    async def wiki(self, ctx, *, query):
        '''Search up something on wikipedia'''
        em = discord.Embed(title=str(query))
        em.set_footer(text='Powered by wikipedia.org')
        try:
            result = wikipedia.summary(query)
            if len(result) > 4000:
                em.color = discord.Color.red()
                em.description = f"Result is too long. View the website [here](https://wikipedia.org/wiki/{query.replace(' ', '_')}), or just google the subject."
                return await ctx.send(embed=em)
            em.color = discord.Color.green()
            em.description = result
            await ctx.send(embed=em)
        except wikipedia.exceptions.DisambiguationError as e:
            em.color = discord.Color.red()
            options = '\n'.join(e.options)
            em.description = f"**Options:**\n\n{options}"
            await ctx.send(embed=em)
        except wikipedia.exceptions.PageError:
            em.color = discord.Color.red()
            em.description = 'Error: Page not found.'
            await ctx.send(embed=em)
    
    @commands.command(name="Urban dictionary",aliases=["ud", "UD"])
    async def urbandictionary(self, ctx, term):
        em = discord.Embed(title=str(term))
        em.set_footer(text='Powered by urbandictionary.com')
        em.color = discord.Colour.orange()
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term":term.lower()}

        headers = {
                    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
                    'x-rapidapi-key': RAPID
                    }
        async with ClientSession() as session:
            async with session.get(url, headers=headers, params=querystring) as response:
                r = await response.json()
                em.description = r['list'][0]['definition']
                await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Utility(bot))
