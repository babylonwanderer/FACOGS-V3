from .raffle import fleetraffle


def setup(bot):
    bot.add_cog(fleetraffle(bot))
