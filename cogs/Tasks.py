import discord
import datetime

from discord.ext import tasks, commands
from BotConfig import BotConfig
from jasper import db

def setup(client: discord.Client):
    client.add_cog(Tasks(client))

class Tasks(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client
        self.identification_check.start()
        self.identification_message.start()
        self.mute_checker.start()
        self.memberCount.start()

    def cog_unload(self):
        self.identification_check.cancel()
        self.identification_message.cancel()
        self.mute_checker.cancel()
        self.memberCount.cancel()
    
    mute = db["Mutes"]

    #4 hour check
    @tasks.loop(minutes = 45)
    async def identification_check(self):
        await self.client.wait_until_ready()
        guild = self.client.get_guild(BotConfig.serverID())
        roleAlumni = discord.utils.get(guild.roles, name = 'Alumni')
        role12 = discord.utils.get(guild.roles, name = 'Grade 12')
        role11 = discord.utils.get(guild.roles, name = 'Grade 11')
        role10 = discord.utils.get(guild.roles, name = 'Grade 10')
        role9 = discord.utils.get(guild.roles, name = 'Grade 9')
        roleOtherSchools = discord.utils.get(guild.roles, name = 'Other Schools')
        roleIdentify = discord.utils.get(guild.roles, name = 'Please Identify Yourself!')
        roleBot = discord.utils.get(guild.roles, name = 'Bot')
        roles = [roleBot, roleAlumni, role12, role11, role10, role9, roleOtherSchools]

        for member in guild.members:
            for x in roles:
                if x in member.roles:
                    role = True
                    break
                role = False
            if role == False and (datetime.datetime.utcnow() - member.joined_at) > datetime.timedelta(hours = 4):
                try:
                    await member.add_roles(roleIdentify)
                except: 
                    print('') #No perms

    
#7 day check
    @tasks.loop(hours = 4)
    async def identification_message(self):
        task = db["Tasks"]

        await self.client.wait_until_ready()
        channel = self.client.get_channel(BotConfig.channel_identify())
        message_id = task.find_one({"_id": "ID_Message"})["message"]
        
        message = await channel.fetch_message(int(message_id))

        if (datetime.datetime.utcnow() - message.created_at) > datetime.timedelta(days = 6, hours = 6):
            msg = await channel.send("<@&775418642946064494> Please go to <#700563120690561024> to pick your roles. We will remove this role once you've picked a grade, thank you :slight_smile:")
            message_id = msg.id
            task.update_one({"_id": "ID_Message"}, {"$set":{"message": message_id}})

#Mute Checking
    @tasks.loop(minutes = 5)
    async def mute_checker(self):
        await self.client.wait_until_ready()
        guild = self.client.get_guild(700559773028057098)
        logs = self.client.get_channel(850777492297875467)
        muted = discord.utils.get(guild.roles, name = 'Muted')
        date = datetime.datetime.now()
        for x in self.mute.find({}):
            id = x["_id"]
            member = await guild.fetch_member(int(id))
            id = x["channel"]
            channel = self.client.get_channel(int(id))
            if datetime.datetime.now() >= x["time"]:
                await member.remove_roles(muted)
                user = {"_id": member.id}
                self.mute.delete_one(user)

                embed = discord.Embed(color = 0xFFCB00)
                embed.set_author(name = member.name + '#' + member.discriminator + ' has been unmuted', icon_url = member.avatar_url)
                embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

                embed_logs = discord.Embed(color = 0xFFCB00)
                embed_logs.set_author(name = 'Jasper [BOT]', icon_url = self.client.user.avatar_url)
                embed_logs.add_field(name = 'Unmuted', value = member.mention, inline = True)
                embed_logs.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

                await channel.send(embed = embed)
                await logs.send(embed = embed_logs)

#Member Count Update
    @tasks.loop(hours = 1)
    async def memberCount(self):
        await self.client.wait_until_ready()
        guild = self.client.get_guild(700559773028057098)
        vc: discord.channel.VoiceChannel = self.client.get_channel(BotConfig.channel_membercount())
        members = len([m for m in guild.members if not m.bot])
        await vc.edit(reason = 'New User Joined', name = '👻 Member Count: ' + str(members))

#SHUT UP BOYUAN
    @commands.Cog.listener()
    async def on_typing(self, channel: discord.TextChannel, member: discord.Member, when):
        try:
            if channel.guild.id == 700559773028057098:
                if member.id == 412316765918461955:
                    await channel.send(f'SHUT THE UP BOYUAN, DONT EVEN FINISH TYPING', delete_after = 8.0)
        except AttributeError:
            pass