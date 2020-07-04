from redbot.core import commands

class stun(commands.Cog):
    """Stuns the user mentioned """
    
    @commands.command()
    async def stun(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
