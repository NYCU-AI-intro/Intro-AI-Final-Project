import discord
from discord.ext import commands
import asyncio, os, keep_alive
from dotenv import load_dotenv
import logging

load_dotenv()
logging.getLogger().setLevel(logging.ERROR)


my_secret = os.environ['bot_token']

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='=', intents=intents, help_command=None)

# 當機器人完成啟動
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")


async def load_all_extentions():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')


async def main():
    keep_alive.keep_alive()
    await load_all_extentions()
    await bot.start(my_secret)


asyncio.run(main())

"""
@bot.command()
async def load(ctx, extension):
    name = ctx.author
    if str(name) == 'qoopercy':
        await bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} successfully loaded')
"""
