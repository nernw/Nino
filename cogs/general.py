from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'🏓 Pong! Ping là {latency}ms')

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Xin chào! Tôi là bot Nino 🤖")
        

async def setup(bot):
    await bot.add_cog(General(bot))
