from redbot.core import commands

class Trek(commands.Cog):
    """Trek Stuff"""

    @commands.command()
    async def scan(self, ctx):
        """Scans a user"""
        # Your code will go here
        await ctx.send("I can do stuff!")
