import discord
import cogs._events as _events

from discord.ext import commands

def setup(client: discord.Client):
    client.add_cog(Events(client))

class Events(commands.Cog):
    def __init__(self, client: discord.Client):
        self.client = client 

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        #
        await _events._on_message(self.client, message)

    @commands.Cog.listener()
    async def on_ready(self):
        await _events._on_ready(self.client)

    @commands.Cog.listener() 
    async def on_member_join(self, member: discord.Member):
        await _events._on_member_join(self.client, member)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        _events._on_member_remove(self.client, member)

#Identified Themself
    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        await _events._on_member_update(self.client, before, after)


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