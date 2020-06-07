import discord
from discord.ext import commands


class MessageAnalyserCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')

    @commands.Cog.listener()
    async def on_message(self, message):
        # Boolean values to check if the message is FAQ related or LFG related
        guilty_FAQ = False
        guilty_LFG = False
        print(str(message.author)+' sent a message')
        # Ensures that the message is not coming from the bot. Todo: add a list of IDs
        #                                                            for all bots on the server
        if message.author.id != 718190488372641823:
            if message[-1] == '?':
                # Todo: most likely a binary search
                guilty_FAQ = search_FAQ(message)
            # Todo: most likely a binary search
            guilty_LFG = search_LFG(message)
        # Todo: routine that sends a message relative to the type of phrase read.
        #       The parameter will end up being attached to the end of a named file/
        #       piece of code that sends out the string.
        if guilty_FAQ :
            deploy_message('FAQ')
            # This is to ensure that the bot does not send out two messages as
            # you cannot have a message represent FAQ and LFG. This is a bit shakey as of now
            guilty_LFG = False
        elif guilty_LFG : deploymessage('LFG')


def setup(client):
    client.add_cog(MessageAnalyserCog(client))
