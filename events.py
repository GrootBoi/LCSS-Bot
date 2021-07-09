import discord
import random
import datetime

from discord.ext import tasks, commands
from jasper import db

class events(commands.Cog):

    def __init__(self, client):
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
    task = db["Tasks"]

#on_message
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        date = datetime.datetime.now()
        dms = self.client.get_channel(857643372944293888)
        hi = ['hello', 'hi', 'hey', 'howdy']
        bye = ['bye', 'goodbye', 'bye bye', 'goodnight', 'gn', 'cya', 'see ya', 'adios', 'byee']
        howareyou = ['how are you', 'how are you?', 'how r u', 'how are u', 'how r you', 'how r u?', 'how are u?', 'how r you?', 'whats up?', "what's up?", 'whats up', "what's up"]
        disagreement = ['fuck you bot', 'shut up bot', 'shutup bot', 'fuck u bot', 'fuk you bot', 'fuck u bot', 'fuck off bot', 'fuk off bot']
        if message.author == self.client.user or message.author.bot:
            pass
        elif message.guild == None:
            embed = discord.Embed(title = 'DM Message', description = message.content, color = 0xFFCB00)
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            embed.add_field(name = 'Reply:', value = f'`!dm {message.author.id} `')
            embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            await dms.send(embed = embed)
        elif message.content.lower() in hi:
            await message.channel.trigger_typing()
            responses = ['Hello', 'Greetings!', 'Howdy', 'Hi!!', 'Hey', 'Helloooooo', 'sup', 'WASSSSUP', 'WAZZUP!', 'Yo!']
            await message.channel.send(random.choice(responses))
        elif message.content.lower() in bye:
            await message.channel.trigger_typing()
            responses = ['Bye!', 'Goodbye!', 'See ya!', 'Au revoir', 'k bye']
            await message.channel.send(random.choice(responses))
        elif message.content.lower() in howareyou:
            await message.channel.trigger_typing()
            responses = ['Good!', "I'm great!", 'Awesome!']
            await message.channel.send(random.choice(responses) + ' How about you?')
        elif message.content.lower() in disagreement:
            await message.channel.trigger_typing()
            responses = ['What did I do :(', 'Im sorry', 'screw you', 'fuck you', 'fuck off', 'ok fine', 'no u', ':(', '<@412316765918461955>']
            await message.channel.send(random.choice(responses))
        elif message.content == '69':
            await message.channel.trigger_typing()
            await message.channel.send('Nice')
            await message.add_reaction('🇳')
            await message.add_reaction('🇮')
            await message.add_reaction('🇨')
            await message.add_reaction('🇪')
        elif message.content == '100':
            await message.add_reaction('💯')
        elif message.content == '420':
            await message.channel.trigger_typing()
            await message.channel.send('Nice')
            await message.add_reaction('🌿')
            await message.add_reaction('🇳')
            await message.add_reaction('🇮')
            await message.add_reaction('🇨')
            await message.add_reaction('🇪')
            await message.add_reaction('😎')
        elif self.client.user.mentioned_in(message):
            await message.channel.trigger_typing()
            await message.channel.send('You pinged?')

#on_ready
    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.client.get_channel(760284361814835200)
        await channel.trigger_typing()
        responses = ['DEAD BODY!!!! <@498176822404579330> has been killed, the suspect is still on the loose!', 'I am Online!', 'zoo wee mama',
        'gooooooooooood morninnnnnnnnnnng ~~Vietnam~~ LCSS Discord', "<@536953999593701418> I didn't kill myself last night",
        'Who is ready to either get hugged or killed?', 'Traceback Error: Uhh- idk what is happening',
        "We're no strangers to love\nYou know the rules and so do I\nA full commitment's what I'm thinking of\nYou wouldn't get this from any other guy\nI just wanna tell you how I'm feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nWe've known each other for so long\nYour heart's been aching but you're too shy to say it\nInside we both know what's been going on\nWe know the game and we're gonna play it\nAnd if you ask me how I'm feeling\nDon't tell me you're too blind to see\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give, never gonna give\n(Give you up)\nWe've known each other for so long\nYour heart's been aching but you're too shy to say it\nInside we both know what's been going on\nWe know the game and we're gonna play it\nI just wanna tell you how I'm feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye"]
        await channel.send(random.choice(responses))

#Member Joining
    @commands.Cog.listener() 
    async def on_member_join(self, member: discord.Member):
        guild = self.client.get_guild(700559773028057098)
        welcome = self.client.get_channel(760278876059861073)
        general = self.client.get_channel(760284361814835200)
        vc = self.client.get_channel(734139663903752292)
        if member.guild.id == 700559773028057098:
            embed = discord.Embed(title = 'Welcome fellow Golden Ghost!', description = 'Please read <#700571972362567763> and enjoy your stay!\nAlso stop by <#700563120690561024> to get identified!', color = 0xFFCB00)
            embed.set_author(name = f'{member.name}#{member.discriminator}', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            embed.set_thumbnail(url = member.avatar_url)
            await welcome.send(embed = embed)
            members = len([m for m in guild.members if not m.bot])
            await vc.edit(reason = 'New User', name = '👻 Member Count: ' + str(members))
            try:
                await member.send("Hello Golden Ghost, I am your friendly neighbourhood LCSS Bot! Welcome to the server and be sure to read <#700571972362567763>. Other than that enjoy your stay and I'll see you around!")
            except discord.HTTPException:
                await general.send(f"Hello {member.mention}! Since your DMs have been turned off, I'll do my little speech here. I am your friendly neighbourhood LCSS Bot! Welcome to the server and be sure to read <#700571972362567763>. Other than that enjoy your stay and I'll see you around!")

#Member Leaving
    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        guild = self.client.get_guild(700559773028057098)
        welcome = self.client.get_channel(760278876059861073)
        vc = self.client.get_channel(734139663903752292)
        if member.guild.id == 700559773028057098:
            members = len([m for m in guild.members if not m.bot])
            await vc.edit(reason = 'User Left', name = '👻 Member Count: ' + str(members))
            embed = discord.Embed(title = 'Goodbye fellow Golden Ghost!', description = 'Sorry to see you go!', color = 0xFFCB00)
            embed.set_author(name = f'{member.name}#{member.discriminator}', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
            embed.set_thumbnail(url = member.avatar_url)
            await welcome.send(embed = embed)

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
        guild = self.client.get_guild(700559773028057098)
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
                await member.add_roles(roleIdentify)
    
#7 day check
    @tasks.loop(hours = 4)
    async def identification_message(self):
        await self.client.wait_until_ready()
        channel = self.client.get_channel(811602544769761281)
        message = self.task.find({"_id": "ID_Message"})
        for id in message:
            message_id = id["message"]
        message = await channel.fetch_message(int(message_id))
        if (datetime.datetime.utcnow() - message.created_at) > datetime.timedelta(days = 6, hours = 6):
            msg = await channel.send("<@&775418642946064494> Please go to <#700563120690561024> to pick your roles. We will remove this role once you've picked a grade, thank you :slight_smile:")
            message_id = msg.id
            self.task.update_one({"_id": "ID_Message"}, {"$set":{"message": message_id}})

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
        vc = self.client.get_channel(734139663903752292)
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

def setup(client):
    client.add_cog(events(client))