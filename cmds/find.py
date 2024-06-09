import discord
from discord.ext import commands


class Cog_Extension(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


class Find(Cog_Extension):

  @commands.command()
  async def test(self, ctx):
    await ctx.send('Hello world')

  
  '''
  @commands.command()
  async def find(self, ctx,  *, msg):
    

    await ctx.send(f"<@{ctx.author.id}> 為你推薦以下論文\n")

      
    with open('paper_txt/exampleOutput.txt', 'r', encoding='utf8') as ptxt:

      ptxt_list = ptxt.readlines()

      #前處理 分中英

      Eng_list = []
      Che_list = []
      
      for line in ptxt_list:

        if line.startswith('英文'):
          Eng_list.append(line)
        if line[0:4] == 'http':
          if msg in line:
            await ctx.send(line)]
        text = ptxt.read()
        await ctx.send(text)
  '''
      

async def setup(bot):
  await bot.add_cog(Find(bot))
