import discord
import datetime
from jasper import db
from BotConfig import BotConfig

async def sendIdentificationMessageHandler(client: discord.client):
    #Ping users who have not identified
    task = db["Tasks"]

    await client.wait_until_ready()
    identifyChannel = client.get_channel(BotConfig.channel_identify())

    #Suggestions
    #Relying on the message id that's sent in the identification channel is cumbersome and error prone
    #Just save a timestamp in the first place isntead of relying on the message id to give you a timestamp

    message_id = task.find_one({"_id": "ID_Message"})["message"]
    message = await identifyChannel.fetch_message(int(message_id))

    if (datetime.datetime.utcnow() - message.created_at) > datetime.timedelta(days = 6, hours = 6):
        msg = await identifyChannel.send("<@&775418642946064494> Please go to <#700563120690561024> to pick your roles. We will remove this role once you've picked a grade, thank you :slight_smile:")
        message_id = msg.id
        task.update_one({"_id": "ID_Message"}, {"$set":{"message": message_id}})
