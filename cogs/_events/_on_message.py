import random
import discord
import datetime

greetings = {
    "triggers": [
        'hello','hi','hey','howdy'
    ],
    "responses":[
        'Hello', 'Greetings!', 'Howdy', 'Hi!!', 'Hey', 
        'Helloooooo', 'sup', 'WASSSSUP', 'WAZZUP!', 'Yo!'
    ]
}

farewells = {
    "triggers": [
        'bye', 'goodbye', 'bye bye', 'goodnight', 'gn', 'cya', 'see ya', 'adios', 'byee'
    ],
    "responses": [
        'Bye!', 'Goodbye!', 'See ya!', 'Au revoir', 'k bye'
    ]
}

howareyou = {
    "triggers": [
        'how are you', 'how are you?', 'how r u', 'how are u', 'how r you', 
        'how r u?', 'how are u?', 'how r you?', 'whats up?', "what's up?", 'whats up', "what's up"
    ],
    "responses": [
        'Good!', "I'm great!", 'Awesome!'
    ]
}

disagreements = {
    "triggers": [
        'fuck you bot', 'shut up bot', 'shutup bot', 'fuck u bot', 
        'fuk you bot', 'fuck u bot', 'fuck off bot', 'fuk off bot'
    ],
    "responses": [
        'What did I do :(', 'Im sorry', 'screw you', 
        'fuck you', 'fuck off', 'ok fine', 'no u', ':(', '<@412316765918461955>'
    ]
}

triggerAndResponse = [greetings, farewells, howareyou, disagreements]

async def _on_message(client: discord.Client, message: discord.Message):
    if message.author == client.user or message.author.bot:
        return

    #I am not entirely sure what this does - Obert
    elif message.guild == None:
        date = datetime.datetime.now()
        dms = client.get_channel(857643372944293888)

        embed = discord.Embed(title = 'DM Message', description = message.content, color = 0xFFCB00)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.add_field(name = 'Reply:', value = f'`!dm {message.author.id} `')
        embed.set_footer(text = f'{date:%B %d, %Y} at {date:%H:%M} EST', icon_url = 'https://cdn.discordapp.com/attachments/818494514867077144/844009816577146900/ghost.jpg')
        await dms.send(embed = embed)

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

    elif client.user.mentioned_in(message):
        await message.channel.trigger_typing()
        await message.channel.send('You pinged?')

    for el in triggerAndResponse:
        if message.content.lower() in el["triggers"]:
            await message.channel.send(random.choice(el["responses"]))