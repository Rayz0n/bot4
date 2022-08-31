import disnake
import time

start = time.monotonic()

bot = commands.Bot(command_prefix = get_prefix, intents = disnake.Intents.all())

@bot.command()
async def uptime(ctx):
 uptime = time.monotonic() - start
 await ctx.send(uptime)
 
bot.run("Token")
