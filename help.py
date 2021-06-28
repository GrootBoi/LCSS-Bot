import discord
import asyncio
import datetime
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    def isitdev(ctx):
        return ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787
    
#Help Command
    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        date = datetime.datetime.now()
        url = 'https://cdn.discordapp.com/attachments/818494514867077144/854036634910326784/lcss.jpg'

    #Table of Contents
        tableOfContents = discord.Embed(title = 'LCSS Help Page', description = 'Main Menu:', color = 0xFFCB00)
        tableOfContents.set_thumbnail(url = url)
        tableOfContents.add_field(name = 'Info ❓', value = 'Find information about roles, members and the server!', inline = False)
        tableOfContents.add_field(name = 'Utilities 📊', value = 'Utilities to help with server operation!', inline = False)
        tableOfContents.add_field(name = 'Fun 🎲', value = 'Fun games and commands for better server experience and interactions!', inline = False)
        if discord.utils.find(lambda r: r.name == 'Staff', ctx.message.guild.roles) in ctx.author.roles:
            tableOfContents.insert_field_at(index = 0, name = 'Moderation 🛡️', value = 'Commands to help moderate the server!', inline = False)
        if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
            tableOfContents.insert_field_at(index = 0, name = 'Dev 🛠️', value = 'Developer commands', inline = False)
            tableOfContents.insert_field_at(index = 6, name = 'Test 🚧', value = 'Commands in testing', inline = False)
        tableOfContents.add_field(name = 'Exit ❌', value = 'Click ❌ to exit', inline = False)
        tableOfContents.set_footer(text = 'React with the emote corresponding to the category to find out more', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

    #Dev Page
        dev = discord.Embed(title = 'LCSS Help Page', description = '🛠️ Dev Commands:', color = 0xFFCB00)
        dev.set_thumbnail(url = url)
        dev.add_field(name = '!cohortembed', value = 'Sends the cohort embed', inline = False)
        dev.add_field(name = '!cohortpurge [Aliases = !cp]', value = 'Purges people of cohort roles', inline = False)
        dev.add_field(name = '!dm @User', value = 'DM someone in the server through the bot', inline = False)
        dev.add_field(name = '!ghost (message)', value = 'Send a bot message in LCSS general with pings', inline = False)
        dev.add_field(name = '!ghostping @User [Aliases = !gp]', value = 'Ghostping someone', inline = False)
        dev.add_field(name = '!gradeshuffle [Aliases = !gs]', value = 'Shuffles all the grades up', inline = False)
        dev.add_field(name = '!id', value = 'Sends the identification embed', inline = False)
        dev.add_field(name = '!interact (message)', value = 'Send a bot message in LCSS general without pings', inline = False)
        dev.add_field(name = '!rules', value = 'Sends the rules embed', inline = False)
        dev.add_field(name = '!selfpromote', value = 'Promotes user to have botperms role', inline = False)
        dev.add_field(name = '!talk (channel id) (message)', value = 'Send a bot message to anywhere the bot is in', inline = False)
        dev.add_field(name = 'Return ◀️', value = 'Click ◀️ to return', inline = False)
        dev.add_field(name = 'Exit ❌', value = 'Click ❌ to exit', inline = False)
        dev.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

    #Moderation Page
        moderation = discord.Embed(title = 'LCSS Help Page', description = '🛡️ Moderation Commands:', color = 0xFFCB00)
        moderation.set_thumbnail(url = url)
        moderation.add_field(name = '!ban @User (Reason)', value = 'Bans a user from the server\nYou will need ban perms', inline = False)
        moderation.add_field(name = '!clear (# of messages) *(@User)', value = 'Clears messages from the server\nYou will need Manage Messages Perms', inline = False)
        moderation.add_field(name = '!cmute @User (Reason)', value = 'Mutes a user from <#760627161920045087>', inline = False)
        moderation.add_field(name = '!cunmute @User', value = 'Unmutes a user from <#760627161920045087>', inline = False)
        moderation.add_field(name = '!imute @User (Reason)', value = 'Mutes a user from sending attachments and embeds', inline = False)
        moderation.add_field(name = '!infractions @User', value = 'Displays the number of infractions the user has', inline = False)
        moderation.add_field(name = '!iunmute @User', value = 'Unmutes a user from sending attachments and embeds', inline = False)
        moderation.add_field(name = '!kick @User (Reason)', value = 'Kicks the user from the server\nYou will need Kick Perms', inline = False)
        moderation.add_field(name = '!mute @User (Duration: 0h0m0s) (Reason)', value = 'Mutes a user in the server', inline = False)
        moderation.add_field(name = '!pmute @User (Reason)', value = 'Permanently mutes a user in the server', inline = False)
        moderation.add_field(name = '!removewarn @User (Warn ID)', value = 'Removes a specific warn from a user', inline = False)
        moderation.add_field(name = '!rmute @User (Reason)', value = 'Mutes a user from using reactions', inline = False)
        moderation.add_field(name = '!runmute @User', value = 'Unmutes a user from using reactions', inline = False)
        moderation.add_field(name = '!slowmode (seconds)', value = 'Sets a slowmode for the channel', inline = False)
        moderation.add_field(name = '!softban @User', value = 'Softbans a user / Clearing 1 day of messages from the user\nYou will need ban perms', inline = False)
        moderation.add_field(name = '!unban @User', value = 'Unbans a user from the server\nYou will need ban perms', inline = False)
        moderation.add_field(name = '!unmute @User', value = 'Unmutes a user in the server', inline = False)
        moderation.add_field(name = '!warn @User (reason)', value = 'Warns a user', inline = False)
        moderation.add_field(name = 'Return ◀️', value = 'Click ◀️ to return', inline = False)
        moderation.add_field(name = 'Exit ❌', value = 'Click ❌ to exit', inline = False)
        moderation.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

    #Info Page
        info = discord.Embed(title = 'LCSS Help Page', description = '❓ Info Commands:', color = 0xFFCB00)
        info.set_thumbnail(url = url)
        info.add_field(name = '!avatar @User [Aliases = !av]', value = 'Displays the avatar of the user', inline = False)
        info.add_field(name = '!botinfo', value = 'Displays information of the bot', inline = False)
        info.add_field(name = '!covid', value = 'Displays covid information', inline = False)
        info.add_field(name = '!emotes', value = 'Displays all emotes in the server', inline = False)
        info.add_field(name = '!invite', value = 'Displays permanent invite link', inline = False)
        info.add_field(name = '!leafs', value = 'Displays stats about the Toronto Maple Laughs', inline = False)
        info.add_field(name = '!owner', value = 'Displays owner of the server', inline = False)
        info.add_field(name = '!roleinfo (Role Name) [Aliases = !role]', value = 'Displays information about the role', inline = False)
        info.add_field(name = '!rolelist (Role Name)', value = 'Displays users with that role', inline = False)
        info.add_field(name = '!roles', value = 'Displays all roles in the server', inline = False)
        info.add_field(name = '!schoolstatus [Aliases = !ss]', value = 'Displays status of schools', inline = False)
        info.add_field(name = '!serverinfo [Aliases = !server]', value = 'Displays information about the server', inline = False)
        info.add_field(name = '!staff [Aliases = !mods, !mod]', value = 'Displays the list of staff in the server', inline = False)
        info.add_field(name = '!userinfo @User [Aliases = !user]', value = 'Displays information about a user', inline = False)
        info.add_field(name = 'Return ◀️', value = 'Click ◀️ to return', inline = False)
        info.add_field(name = 'Exit ❌', value = 'Click ❌ to exit', inline = False)
        info.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

    #Utilities Page
        utilities = discord.Embed(title = 'LCSS Help Page', description = '📊 Utilities Commands:', color = 0xFFCB00)
        utilities.set_thumbnail(url = url)
        utilities.add_field(name = '!bc [Aliases = !botcommands]', value = 'Redirects someone to <#789619349903507456>', inline = False)
        utilities.add_field(name = '!emergency [Aliases = !sos]', value = 'Emergency staff ping\nOnly selected people can do this', inline = False)
        utilities.add_field(name = '!gen [Aliases = !general]', value = 'Redirects someone to <#760284361814835200>', inline = False)
        utilities.add_field(name = '!id [Aliases = !identification]', value = 'Redirects someone to <#700563120690561024>', inline = False)
        utilities.add_field(name = '!meme', value = 'Redirects someone to <#760284416848298025>', inline = False)
        utilities.add_field(name = '!pg', value = 'Reminds someone to keep it PG-13 (In memory of Charles)', inline = False)
        utilities.add_field(name = '!ping [Aliases = !pong]', value = 'Returns the bots response time', inline = False)
        utilities.add_field(name = '!poll (Question) [Alises = !vote]', value = 'Creates a poll in <#823041499259207690>\nOnly Staff can use it', inline = False)
        utilities.add_field(name = '!roleping (seconds) (role)', value = 'Allows a role to be pingable for 0 - 45 seconds\nOnly Staff can use it and is limited to <#700600677596004415>, <#847873556725628998>, <#745331414718742569>, and <#701877914001735772>', inline = False)
        utilities.add_field(name = '!st [Aliases = !schooltalk]', value = 'Redirects someone to <#771694740521091114>', inline = False)
        utilities.add_field(name = 'Return ◀️', value = 'Click ◀️ to return', inline = False)
        utilities.add_field(name = 'Exit ❌', value = 'Click ❌ to exit', inline = False)
        utilities.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

    #Fun Page
        fun = discord.Embed(title = 'LCSS Help Page', description = '🎲 Fun Commands:', color = 0xFFCB00)
        fun.set_thumbnail(url = url)
        fun.add_field(name = '!8ball (Question) [Aliases = !eightball]', value = 'Allows user to ask the 8 ball a question', inline = False)
        fun.add_field(name = '!bam @User [Aliases = !bang]', value = f'Throws a hammer at someone with 20% hit success', inline = False)
        fun.add_field(name = '!bann @User (reason)', value = 'False bans a user to give them a scare (hopefully)', inline = False)
        fun.add_field(name = '!boyuan', value = 'Tells Boyuan to go fuck himself while ghost pinging him along with calling him a bunch of nicknames', inline = False)
        fun.add_field(name = '!fys @User [Aliases = !fuckoff, !gfys]', value = 'Tells someone to go fuck themself', inline = False)
        fun.add_field(name = '!hug @User', value = 'Gives your friend a hug', inline = False)
        fun.add_field(name = '!kill @User', value = 'The bot will kill your enemy', inline = False)
        fun.add_field(name = '!revive @User', value = 'The bot will revive a user, be careful who you use this on though', inline = False)
        fun.add_field(name = '!rockpaperscissors [Aliases = !rps]', value = 'Rock Paper Scissors!', inline = False)
        fun.add_field(name = '!rockpaperscissorsstats [Aliases = !rpsstats]', value = 'Rock Paper Scissors Stats', inline = False)
        fun.add_field(name = '!rpsls [Aliases = !rps5]', value = 'Rock Paper Scissors Lizard Spock (RPS with 5 objects)!', inline = False)
        fun.add_field(name = '!rpslsinfo', value = 'Rock Paper Scissors Lizard Spock info', inline = False)
        fun.add_field(name = 'Return ◀️', value = 'Click ◀️ to return', inline = False)
        fun.add_field(name = 'Exit ❌', value = 'Click ❌ to exit', inline = False)
        fun.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

    #Test Page
        test = discord.Embed(title = 'LCSS Help Page', description = '🚧 Test Commands:', color = 0xFFCB00)
        test.set_thumbnail(url = url)
        test.add_field(name = '!dbadd', value = 'Adding to Database', inline = False)
        test.add_field(name = '!dbdelete', value = 'Deleting from Database', inline = False)
        test.add_field(name = '!dbedit', value = 'Editing from Database', inline = False)
        test.add_field(name = '!dbget', value = 'Get from Database', inline = False)
        test.add_field(name = '!test', value = 'Something is being tested here...', inline = False)
        test.add_field(name = 'Return ◀️', value = 'Click ◀️ to return', inline = False)
        test.add_field(name = 'Exit ❌', value = 'Click ❌ to exit', inline = False)
        test.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')

    #Sending
        help = await ctx.send(embed = tableOfContents)
        if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
            await help.add_reaction('🛠️')
        if discord.utils.find(lambda r: r.name == 'Staff', ctx.message.guild.roles) in ctx.author.roles:
            await help.add_reaction('🛡️')
        await help.add_reaction('❓')
        await help.add_reaction('📊')
        await help.add_reaction('🎲')
        if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
            await help.add_reaction('🚧')
        await help.add_reaction('❌')

    #Reactions
        try:
            reaction, user = await self.client.wait_for('reaction_add', check = lambda r, u: u == ctx.author and str(r.emoji) in ('🛠️', '🛡️', '📊', '❓', '🎲', '🚧', '❌', '◀️'), timeout = 60)
            for x in range(999):
                if str(reaction.emoji) == '🛠️':
                    await help.edit(embed = dev)
                    await help.remove_reaction('🛠️', member = ctx.author)
                    await help.remove_reaction('🛠️', member = self.client.user)
                    await help.remove_reaction('🛡️', member = self.client.user)
                    await help.remove_reaction('📊', member = self.client.user)
                    await help.remove_reaction('❓', member = self.client.user)
                    await help.remove_reaction('🎲', member = self.client.user)
                    await help.remove_reaction('🚧', member = self.client.user)
                    await help.add_reaction('◀️')
                elif str(reaction.emoji) == '🛡️':
                    await help.edit(embed = moderation)
                    await help.remove_reaction('🛡️', member = ctx.author)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🛠️', member = self.client.user)
                    await help.remove_reaction('🛡️', member = self.client.user)
                    await help.remove_reaction('📊', member = self.client.user)
                    await help.remove_reaction('❓', member = self.client.user)
                    await help.remove_reaction('🎲', member = self.client.user)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🚧', member = self.client.user)
                    await help.add_reaction('◀️')
                elif str(reaction.emoji) == '❓':
                    await help.edit(embed = info)
                    await help.remove_reaction('❓', member = ctx.author)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🛠️', member = self.client.user)
                    if discord.utils.find(lambda r: r.name == 'Staff', ctx.message.guild.roles) in ctx.author.roles:
                        await help.remove_reaction('🛡️', member = self.client.user)
                    await help.remove_reaction('📊', member = self.client.user)
                    await help.remove_reaction('❓', member = self.client.user)
                    await help.remove_reaction('🎲', member = self.client.user)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🚧', member = self.client.user)
                    await help.add_reaction('◀️')
                elif str(reaction.emoji) == '📊':
                    await help.edit(embed = utilities)
                    await help.remove_reaction('📊', member = ctx.author)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🛠️', member = self.client.user)
                    if discord.utils.find(lambda r: r.name == 'Staff', ctx.message.guild.roles) in ctx.author.roles:
                        await help.remove_reaction('🛡️', member = self.client.user)
                    await help.remove_reaction('📊', member = self.client.user)
                    await help.remove_reaction('❓', member = self.client.user)
                    await help.remove_reaction('🎲', member = self.client.user)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🚧', member = self.client.user)
                    await help.add_reaction('◀️')
                elif str(reaction.emoji) == '🎲':
                    await help.edit(embed = fun)
                    await help.remove_reaction('🎲', member = ctx.author)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🛠️', member = self.client.user)
                    if discord.utils.find(lambda r: r.name == 'Staff', ctx.message.guild.roles) in ctx.author.roles:
                        await help.remove_reaction('🛡️', member = self.client.user)
                    await help.remove_reaction('📊', member = self.client.user)
                    await help.remove_reaction('❓', member = self.client.user)
                    await help.remove_reaction('🎲', member = self.client.user)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🚧', member = self.client.user)
                    await help.add_reaction('◀️')
                elif str(reaction.emoji) == '🚧':
                    await help.edit(embed = test)
                    await help.remove_reaction('🚧', member = ctx.author)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🛠️', member = self.client.user)
                    await help.remove_reaction('🛡️', member = self.client.user)
                    await help.remove_reaction('📊', member = self.client.user)
                    await help.remove_reaction('❓', member = self.client.user)
                    await help.remove_reaction('🎲', member = self.client.user)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.remove_reaction('🚧', member = self.client.user)
                    await help.add_reaction('◀️')
                elif str(reaction.emoji) == '◀️':
                    await help.remove_reaction('◀️', member = ctx.author)
                    await help.remove_reaction('◀️', member = self.client.user)
                    await help.remove_reaction('❌', member = self.client.user)
                    await help.edit(embed = tableOfContents)
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.add_reaction('🛠️')
                    if discord.utils.find(lambda r: r.name == 'Staff', ctx.message.guild.roles) in ctx.author.roles:
                        await help.add_reaction('🛡️')
                    await help.add_reaction('❓')
                    await help.add_reaction('📊')
                    await help.add_reaction('🎲')
                    if ctx.author.id == 524001661379936268 or ctx.author.id == 512804342445899787:
                        await help.add_reaction('🚧')
                    await help.add_reaction('❌')
                elif str(reaction.emoji) == '❌':
                    await help.delete()
                    break
                try:
                    reaction, user = await self.client.wait_for('reaction_add', check = lambda r, u: u == ctx.author and str(r.emoji) in ('🛠️', '🛡️', '📊', '❓', '🎲', '🚧', '❌', '◀️'), timeout = 60)
                except asyncio.TimeoutError:
                    await ctx.send(f'Timed Out. Send !help again if you need to.')
                    return
        except asyncio.TimeoutError:
            await ctx.send(f'Timed Out. Send !help again if you need to.')
            return

def setup(client):
    client.add_cog(help(client))
