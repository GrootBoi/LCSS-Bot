import discord
import random
import datetime
import json

from discord.ext import tasks, commands

class events(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.identification_check.start()
        self.identification_message.start()

    def cog_unload(self):
        self.identification_check.cancel()
        self.identification_message.cancel()

#on_message
    @commands.Cog.listener()
    async def on_message(self, message):
        hi = ['hello', 'hi', 'hey', 'howdy']
        bye = ['bye', 'goodbye', 'bye bye', 'goodnight', 'gn', 'cya', 'see ya', 'adios', 'byee']
        howareyou = ['how are you', 'how are you?', 'how r u', 'how are u', 'how r you', 'how r u?', 'how are u?', 'how r you?', 'whats up?', "what's up?", 'whats up', "what's up"]
        disagreement = ['fuck you bot', 'shut up bot', 'shutup bot', 'fuck u bot', 'fuk you bot', 'fuck u bot', 'fuck off bot', 'fuk off bot']
        number = ['69']
        if message.author == self.client.user or message.author.bot:
            return
        if message.content.lower() in hi:
            responses = ['Hello', 'Greetings!', 'Howdy', 'Hi!!', 'Hey', 'Helloooooo', 'sup', 'WASSSSUP', 'WAZZUP!', 'Yo!']
            await message.channel.send(random.choice(responses))
            return
        elif message.content.lower() in bye:
            responses = ['Bye!', 'Goodbye!', 'See ya!', 'Au revoir', 'k bye']
            await message.channel.send(random.choice(responses))
            return
        elif message.content.lower() in howareyou:
            responses = ['Good!', "I'm great!", 'Awesome!']
            await message.channel.send(random.choice(responses) + ' How about you?')
            return
        elif message.content.lower() in disagreement:
            responses = ['What did I do :(', 'Im sorry', 'screw you', 'fuck you', 'fuck off', 'ok fine', 'no u', ':(', '<@412316765918461955>']
            await message.channel.send(random.choice(responses))
            return
        elif message.content in number:
            await message.channel.send('Nice')
            return

#on_ready
    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.client.get_channel(760284361814835200)
        responses = ['DEAD BODY!!!! <@498176822404579330> has been killed, the suspect is still on the loose!', 'I am Online!', 'zoo wee mama',
        'gooooooooooood morninnnnnnnnnnng ~~Vietnam~~ LCSS Discord', "<@536953999593701418> I didn't kill myself last night",
        'Who is ready to either get hugged or killed?', 'Traceback Error: Uhh- idk what is happening']
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
            except discord.Forbidden():
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
        try:
            roleAlumni = discord.utils.get(guild.roles, name = 'Alumni')
            role12 = discord.utils.get(guild.roles, name = 'Grade 12')
            role11 = discord.utils.get(guild.roles, name = 'Grade 11')
            role10 = discord.utils.get(guild.roles, name = 'Grade 10')
            role9 = discord.utils.get(guild.roles, name = 'Grade 9')
            roleOtherSchools = discord.utils.get(guild.roles, name = 'Other Schools')
            roleIdentify = discord.utils.get(guild.roles, name = 'Please Identify Yourself!')
            member = guild.get_member(before.id)
            if roleIdentify in before.roles and after.roles:
                if roleAlumni not in before.roles and roleAlumni in after.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if role12 not in before.roles and role12 in after.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if role11 not in before.roles and role11 in after.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if role10 not in before.roles and role10 in after.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if role9 not in before.roles and role9 in after.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
                if roleOtherSchools not in before.roles and roleOtherSchools in after.roles:
                    await member.remove_roles(roleIdentify, reason = 'User Identified Themself')
        except AttributeError:
            return

#4 hour check
    @tasks.loop(minutes = 30)
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
        for member in guild.members:
            if roleBot not in member.roles:
                if roleAlumni not in member.roles:
                    if role12 not in member.roles:
                        if role11 not in member.roles:
                            if role10 not in member.roles:
                                if role9 not in member.roles:
                                    if roleOtherSchools not in member.roles:
                                        if (datetime.datetime.utcnow() - member.joined_at) > datetime.timedelta(hours = 4):
                                            await member.add_roles(roleIdentify)
    
#7 day check
    @tasks.loop(hours = 4)
    async def identification_message(self):
        await self.client.wait_until_ready()
        channel = self.client.get_channel(811602544769761281)
        with open('id.json', 'r') as f:
            data = json.load(f)
            for num in data['Last Message']:
                id = int(num['message'])
            message = await channel.fetch_message(id)
            if (datetime.datetime.utcnow() - message.created_at) > datetime.timedelta(days = 7):
                msg = await channel.send("<@&775418642946064494> Please go to <#700563120690561024> to pick your roles. We will remove this role once you've picked a grade, thank you :slight_smile:")
                newid = msg.id
                with open('id.json', 'r') as f:
                    data = json.load(f)
                    data['Last Message'] = []
                    data['Last Message'].append({
                        'message': newid
                    })
                    with open('id.json', 'w') as f:
                        json.dump(data, f, indent = 4)

def setup(client):
    client.add_cog(events(client))