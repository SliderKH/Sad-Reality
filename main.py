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
    role = member.guild.get_role(role_id=settings.member_role_id)  # role_id on join
    await member.add_roles(role)
    welcome = bot.get_channel(settings.welcome_chat_id)  # chat_id
    embed = discord.Embed(
        title=f"Добро пожаловать! {member.mention}",
        description=f"Получите роли в #📃info !",
        color=discord.Color.red()
    )
    embed.set_thumbnail(url=settings.logo_url)
    await welcome.send(embed=embed)


bot.run(settings.token)