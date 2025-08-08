import discord
import os
import requests
from discord.ext import commands
from keep_alive import keep_alive

from config import config
from musicbot.audiocontroller import AudioController
from musicbot.settings import Settings
from musicbot import utils
from musicbot.utils import guild_to_audiocontroller, guild_to_settings

from musicbot.commands.general import General
import time

try:
  os.system("pip install -U PyNaCl")
  os.system("pip install -U discord.py[voice]")
  time.sleep(3)
except Exception:
  print("error")

# if module error pops up got to shell and do (pip install -U discord.py[voice])

r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")


initial_extensions = ['musicbot.commands.music',
                      'musicbot.commands.general', 'musicbot.plugins.button']
bot = commands.Bot(command_prefix=config.BOT_PREFIX, pm_help=True, case_insensitive=True,intents=discord.Intents.default())


if __name__ == '__main__':

    config.ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
    config.COOKIE_PATH = config.ABSOLUTE_PATH + config.COOKIE_PATH

    if config.BOT_TOKEN == "":
        print("Error: No bot token!")
        exit

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)


@bot.event
async def on_ready():
    print(config.STARTUP_MESSAGE)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Music, type {}help".format(config.BOT_PREFIX)))

    for guild in bot.guilds:
        await register(guild)
        print("Joined {}".format(guild.name))

    print(config.STARTUP_COMPLETE_MESSAGE)
    
    keep_alive()


@bot.event
async def on_guild_join(guild):
    print(guild.name)
    await register(guild)


async def register(guild):

    guild_to_settings[guild] = Settings(guild)
    guild_to_audiocontroller[guild] = AudioController(bot, guild)

    vc_channels = guild.voice_channels
    await guild.me.edit(nick=guild_to_settings[guild].get('default_nickname'))
    start_vc = guild_to_settings[guild].get('start_voice_channel')
    if start_vc != None:
        for vc in vc_channels:
            if vc.id == start_vc:
                await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])
                await General.udisconnect(self=None, ctx=None, guild=guild)
                try:
                    await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])
                except Exception as e:
                    print(e)
    else:
        await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
        await General.udisconnect(self=None, ctx=None, guild=guild)
        try:
            await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
        except Exception as e:
            print(e)


bot.run(config.BOT_TOKEN, reconnect=True)