import discord
import cogs._tasks as _tasks

from Utils import Utils
from discord.ext import tasks, commands

def setup(client: discord.Client):
    client.add_cog(Tasks(client))

class Tasks(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
        self.identification_check.start()
        self.send_identification_message()
        self.check_expired_mutes.start()
        self.update_membercount.start()

    def cog_unload(self):
        self.identification_check.cancel()
        self.send_identification_message.cancel()
        self.check_expired_mutes.cancel()
        self.update_membercount.cancel()

    @tasks.loop(minutes = 45)
    async def identification_check(self):
        #Add identification role to members if they haven't recieved a role 
        try:
            await _tasks.identificationCheckHandler(self.client)
        except Exception as e:
            Utils.log_error(e)
        
    @tasks.loop(hours = 4)
    async def send_identification_message(self):
        #Ping users who have not identified
        try:
            await _tasks.sendIdentificationMessageHandler(self.client)
        except Exception as e:
            Utils.log_error(e)

    @tasks.loop(minutes = 5)
    async def check_expired_mutes(self):
        try:
            await _tasks.checkExpiredMutesHandler(self.client)
        except Exception as e:
            Utils.log_error(e)

    @tasks.loop(hours = 1)
    async def update_membercount(self):
        try:
            await _tasks.updateMemberountHandler(self.client)
        except Exception as e:
            Utils.log_error(e)
