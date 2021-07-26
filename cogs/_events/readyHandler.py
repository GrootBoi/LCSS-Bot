import random
import discord
import datetime
from Utils import Utils
from BotConfig import BotConfig

responses = [
    'DEAD BODY!!!! <@498176822404579330> has been killed, the suspect is still on the loose!', 
    'I am Online!', 'zoo wee mama',
    'gooooooooooood morninnnnnnnnnnng ~~Vietnam~~ LCSS Discord', 
    "<@536953999593701418> I didn't kill myself last night",
    'Who is ready to either get hugged or killed?', 
    'Traceback Error: Uhh- idk what is happening',
    "We're no strangers to love\nYou know the rules and so do I\nA full commitment's what I'm thinking of\nYou wouldn't get this from any other guy\nI just wanna tell you how I'm feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nWe've known each other for so long\nYour heart's been aching but you're too shy to say it\nInside we both know what's been going on\nWe know the game and we're gonna play it\nAnd if you ask me how I'm feeling\nDon't tell me you're too blind to see\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give, never gonna give\n(Give you up)\nWe've known each other for so long\nYour heart's been aching but you're too shy to say it\nInside we both know what's been going on\nWe know the game and we're gonna play it\nI just wanna tell you how I'm feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye"
]

async def readyHandler(client: discord.Client):
    date = datetime.datetime.now()
    Utils.log_info(f'{client.user.name} is connected at {date:%B %d, %Y} at {date:%H:%M} EST!')

    channel = client.get_channel(BotConfig.channel_general())
    await channel.trigger_typing()
    await channel.send(random.choice(responses))