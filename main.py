import discord
from discord.ext import commands
import settings

bot = commands.Bot(command_prefix=('!'), intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print("I`m Ready")
    await bot.change_presence(activity=discord.Game(name='Sad Reality'))

@bot.event
async def on_member_join(member):
    role = member.guild.get_role(settings.member_role_id)
    await member.add_roles(role)
    welcome = bot.get_channel(settings.welcome_chat_id)
    info_chat = bot.get_channel(settings.info_chat_id)
    embed = discord.Embed(
        title="Добро пожаловать!",
        description=f"{member.mention},\nПолучите роли в {info_chat.mention} !",
        color=discord.Color.red()
    )
    embed.set_footer(
        icon_url=settings.logo_url,
        text="Sad Reality")
    await welcome.send(embed=embed)


bot.run(settings.token)