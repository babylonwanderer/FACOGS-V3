from .stun import stun

def setup(bot):
    bot.add_cog(stun(bot))
