import time
import discord
import random
import datetime
from discord import Embed
from discord.ext import commands

bot = commands.Bot(command_prefix = '>>')
    
class flow(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.last_timeStamp = datetime.datetime.utcfromtimestamp(0)
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Listener Cog has been loaded\n-----")

    @commands.Cog.listener()
    async def on_message(self, message):
      if(message.author.id == bot.user.id):
        return
      else:
        time_difference = (datetime.datetime.utcnow() - self.last_timeStamp).total_seconds()
        
        if time_difference < 5:
            print("time difference too short")
            # Don't do anything and return
            return
        
        elif 'candice' in message.content.lower(): 
            mention1 = message.author.mention
            response = f"{mention1}, deez nuts fit in ur mouth!"
            await message.channel.send(response)
            self.last_timeStamp =datetime.datetime.utcnow()
        
        elif 'Candice' in message.content: 
            mention1 = message.author.mention
            response = f"{mention1}, deez nuts fit in ur mouth!"
            await message.channel.send(response)
            self.last_timeStamp =datetime.datetime.utcnow()

    @commands.Cog.listener()
    async def on_message(self, message):
        if(message.author.id == bot.user):
            return

        elif 'CENSORED' in message.content.lower(): 
            mention1 = message.author.mention
            await message.delete()
            response = f"{mention1}, that word is taboo (not allowed)"
            await message.channel.send(response)
            
def setup(bot):
  bot.add_cog(flow(bot))
