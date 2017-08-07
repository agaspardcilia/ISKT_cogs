import discord
from discord.ext import commands

class ISKT:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def canRead(self, ctx, chan : discord.Channel = None ):
        result = ""
        server = ctx.message.server
        
        if chan is None: # Is the an argument ?
            result += "No given channel, using channel used to send the command.\n"
            channel = ctx.message.channel
        else:
            channel = server.get_channel(chan.id)
            if channel is None: # Does this channel exists ?
                result += "Can't find this channel, using channel used to send the command.\n"
                channel = ctx.message.channel

        members = server.members # Every members of the server. TODO there might be a way to only get users that has a role.

        result += "**__List of users who can access " + channel.mention + " : __**\n"

        for m in members:
            if channel.permissions_for(m).read_messages :
                result += m.name + "#" + m.discriminator + "\n"

        await self.bot.say(result)

def setup(bot):
    bot.add_cog(ISKT(bot))