import discord
from discord.ext import commands
from LLM.RAG import Agent

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


    '''按鈕刪除
    button.disabled = True
    button.view.remove_item(button)
    await interaction.response.edit_message(content="Hello world", view=button.view)
    '''
    
class Output(Cog_Extension):

  def __init__(self, bot):
    super().__init__(bot)
    print('init')
    self.LLMAgent = Agent()
  

  @commands.command()
  async def search(self, ctx, *, msg):
    
    Eng_output, Che_output = self.LLMAgent.ask_question(msg)

    judge = "etoc"

    view = Translate_Button(Eng_output, Che_output, judge)

    await ctx.send(view = view, content = Eng_output)

  

async def setup(bot):
  await bot.add_cog(Output(bot))
