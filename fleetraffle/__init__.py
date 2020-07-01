from .raffle import FleetRaffle


def setup(bot):
    bot.add_cog(FleetRaffle(bot))
