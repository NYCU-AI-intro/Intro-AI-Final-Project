import discord
from discord.ext import commands
import time
import json

with open('json/setting.json', 'r', encoding='utf8') as jfile:
  jdata = json.load(jfile)
with open('json/help.json', 'r', encoding='utf8') as hfile:
  hdata = json.load(hfile)


class Main(commands.Cog): # 繼承commands.Cog

  def __init__(self, bot):
    self.bot = bot

# 上線提示

  @commands.Cog.listener()
  async def on_ready(self):
    print('bot is online')

# 延遲顯示

  @commands.command()
  async def ping(self, ctx):
    pin = round(1000 * self.bot.latency)
    await ctx.send(f'現在的延遲是{pin}ms左右')

# reload

  @commands.command()
  async def reload(self, ctx, *, extension):
    
    name = ctx.author
    
    if str(name) == 'qoopercy':
      
      await self.bot.reload_extension(f'cmds.{extension}')

      jdata["ver_3rd"] += 1
      with open("json/setting.json", "w+", encoding='utf8') as fp:
        json.dump(jdata, fp, sort_keys=True, indent=4)

      await ctx.send(f'{extension} successfully reloaded\nver {jdata["ver_1st"]}.{jdata["ver_2nd"]}.{jdata["ver_3rd"]}')

# unload

  @commands.command()
  async def unload(self, ctx, *, extension):
    name = ctx.author
    if str(name) == 'qoopercy':
      await self.bot.unload_extension(f'cmds.{extension}')
      await ctx.send(f'{extension} successfully unloaded')

# load

  @commands.command()
  async def load(self, ctx, *, extension):
    name = ctx.author
    if str(name) == 'qoopercy':
      await self.bot.load_extension(f'cmds.{extension}')
      await ctx.send(f'{extension} successfully loaded')

# 版本
  @commands.command()
  async def ver(self, ctx):
    await ctx.send(f'ver {jdata["ver_1st"]}.{jdata["ver_2nd"]}.{jdata["ver_3rd"]}')

# 刪除訊息

  @commands.command()
  async def clean(self, ctx, num: int):
    name = ctx.author
    if str(name) == 'qoopercy':
      await ctx.message.delete()
      await ctx.send('3秒後刪除訊息')
      time.sleep(3)
      await ctx.channel.purge(limit=num + 1)
    else:
      await ctx.send(ctx.author)

# 檔案位置

  @commands.command()
  async def data(self, ctx):
      await ctx.send("https://replit.com/@percytsaics12/Discord-LLM-Read-Paper-Bot")


# help

  @commands.command()
  async def help(self, ctx):
    help_des = hdata["help_des"]
    await ctx.channel.purge(limit = 1) 
    await ctx.send(help_des)


async def setup(bot):
  await bot.add_cog(Main(bot))
