import discord
import datetime
import os
import cogs._events as _events

from dotenv import load_dotenv
from discord.ext import tasks, commands
from jasper import db

load_dotenv()

#later, condense ids into a config object
MEMBERCOUNT_CHANNEL_ID = int(os.getenv('MEMBERCOUNT_CHANNEL_ID'))
WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID'))
SERVER_ID = int(os.getenv('SERVER_ID'))
LOG_CHANNEL_ID = int(os.getenv('LOG_CHANNEL_ID'))
PUNISHMENT_CHANNEL_ID = int(os.getenv('PUNISHMENT_CHANNEL_ID'))
BOTSETUP_CHANNEL_ID = int(os.getenv('BOTSETUP_CHANNEL_ID'))
IDENTIFY_CHANNEL_ID = int(os.getenv('IDENTIFY_CHANNEL_ID'))
GENERAL_CHANNEL_ID = int(os.getenv('GENERAL_CHANNEL_ID'))

class events(commands.Cog):
    def __init__(self, client):
        self.client: discord.Client = client
        self.identification_check.start()
        self.identification_message.start()
        self.mute_checker.start()
        self.memberCount.start()

    def setup(client):
        client.add_cog(events(client))

    def cog_unload(self):
        self.identification_check.cancel()
        self.identification_message.cancel()
        self.mute_checker.cancel()
        self.memberCount.cancel()

    mute = db["Mutes"]

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        await _events._on_message(self.client, message)

    @commands.Cog.listener()
    async def on_ready(self):
        await _events._on_ready(self.client, GENERAL_CHANNEL_ID)

    @commands.Cog.listener() 
    async def on_member_join(self, member: discord.Member):
        await _events._on_member_join(
            self.client, 
            member, 
            SERVER_ID, 
            WELCOME_CHANNEL_ID, 
            GENERAL_CHANNEL_ID, 
            MEMBERCOUNT_CHANNEL_ID
        )

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        _events._on_member_remove(
            self.client, member, 
            SERVER_ID, 
            WELCOME_CHANNEL_ID, 
            MEMBERCOUNT_CHANNEL_ID
        )

#Identified Themself
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = self.client.get_guild(700559773028057098)
        roleAlumni = discord.utils.get(guild.roles, name = 'Alumni')
        role12 = discord.utils.get(guild.roles, name = 'Grade 12')
        role11 = discord.utils.get(guild.roles, name = 'Grade 11')
        role10 = discord.utils.get(guild.roles, name = 'Grade 10')
        role9 = discord.utils.get(guild.roles, name = 'Grade 9')
        roleOtherSchools = discord.utils.get(guild.roles, name = 'Other Schools')
        roleIdentify = discord.utils.get(guild.roles, name = 'Please Identify Yourself!')
        member = guild.get_member(before.id)
        roles = [roleAlumni, role12, role11, role10, role9, roleOtherSchools]
        for x in roles:
            try:
                if roleIdentify in before.roles and after.roles:
                    if x not in before.roles and x in after.roles:
                        await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
            except AttributeError:
                return

#4 hour check
    @tasks.loop(minutes = 45)
    async def identification_check(self):
        await self.client.wait_until_ready()
        guild = self.client.get_guild(SERVER_ID)
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
        channel = self.client.get_channel(IDENTIFY_CHANNEL_ID)
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
        vc: discord.channel.VoiceChannel = self.client.get_channel(MEMBERCOUNT_CHANNEL_ID)
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

#Rick Roll
    #@commands.Cog.listener()
    #async def on_voice_state_update(self, member, before, after):
        #guild = self.client.get_guild(700559773028057098)
        #if member.guild == guild and not member.bot:
            #if not before.channel and after.channel:
                #vc = member.voice.channel
                #await vc.connect()
                #voice = discord.utils.get(self.client.voice_clients, guild = guild)
                #ytdl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192',}],}
                #ytdl = youtube_dl.YoutubeDL(ytdl_opts)
                #extract = ytdl.extract_info('https://www.youtube.com/watch?v=dQw4w9WgXcQ', download = False)
                #content = discord.FFmpegOpusAudio(extract['formats'][0]['url'], executable = 'C:/ffmpeg/ffmpeg.exe', options = '-vn', before_options = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5')
                #voice.play(content)
                #while voice.is_playing():
                    #await asyncio.sleep(230)
                #else:
                    #await voice.disconnect()
            #if before.channel and not after.channel:
                #voice = discord.utils.get(self.client.voice_clients, guild = guild)
                #if voice != None:
                    #voice = discord.utils.get(self.client.voice_clients, guild = guild)
                    #await voice.disconnect()

#Counting
    #@commands.Cog.listener()
    #async def on_member_update(self, before, after):
        #guild = self.client.get_guild(700559773028057098)
        #counting = self.client.get_channel(760627161920045087)
        #if before.id == 510016054391734273:
            #if before.raw_status != 'offline' and after.raw_status == 'offline':
                #await counting.send('The Counting bot is offline. The channel will be locked for the time being.')
                #await counting.set_permissions(guild.default_role, send_message = False)

    #@commands.Cog.listener()
    #async def on_member_update(self, before, after):
        #guild = self.client.get_guild(700559773028057098)
        #counting = self.client.get_channel(760627161920045087)
        #if before.id == 510016054391734273:
            #if before.raw_status == 'offline' and after.raw_status != 'offline':
                #await counting.send('The Counting bot is back online. The channel is now unlocked.')
                #await counting.set_permissions(guild.default_role, send_message = True)