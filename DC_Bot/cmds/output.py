import discord
from discord.ext import commands

#from translate_button import etoc_Button

class Cog_Extension(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


class Translate_Button(discord.ui.View):

  def __init__(self, Eng_txt, Che_txt, judge):
    super().__init__()
    self.Eng_txt = Eng_txt
    self.Che_txt = Che_txt
    self.judge = judge

  @discord.ui.button(label="Translate", style = discord.ButtonStyle.success, custom_id = "Translate_button")

  async def buttonEvent(self, interaction, button):

    if self.judge == 'etoc':
      await interaction.response.edit_message(content = self.Che_txt)
      self.judge = 'ctoe'

    elif self.judge == 'ctoe':
      await interaction.response.edit_message(content = self.Eng_txt)
      self.judge = 'etoc'


    '''
    button.disabled = True
    button.view.remove_item(button)
    await interaction.response.edit_message(content="Hello world", view=button.view)
    '''
    
class Output(Cog_Extension):

  @commands.command()
  async def output(self, ctx):

    #Eng_output, Che_output = "abc", "你好"  #侑哲函式回傳

  
    Eng_output = "cfd"
    Che_output = "你好"

    judge = "etoc"

    view = Translate_Button(Eng_output, Che_output, judge)


    await ctx.send(view = view, content = Eng_output)

    await ctx.send(f"{Eng_output}\n\n")

    await ctx.send(f"{Che_output}\n\n")

  '''@commands.command()
  async def btest(self, ctx):

    await ctx.send('btest')

    view = Translate_Button()

    await ctx.send(view)

    Eng_output, Che_output = "abc", "你好"  #侑哲函式回傳'''


async def setup(bot):
  await bot.add_cog(Output(bot))
