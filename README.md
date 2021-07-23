# LCSS-Bot: Jasper
This is the bot for the LCSS Discord server. 
Uhh, yeah this is what exists so far, feel free to dig into it if you feel!

Download to Desktop, open Command Prompt --> cd desktop --> cd jasper.py

# Dependencies
* discord.py 
* python-dotenv
* pymongo
* pymongo[srv] (optional)
* pytz

# Getting Started
* A `.env` file is required in the project's root directory with the following fields assigned

    DISCORD_TOKEN=Insert bot's token
    MONGODB_URL=Mongodb DB connection url
    BOT_PREFIX=The prefix for commands the bot will respond to

    SERVER_ID=The main server id the bot will reside in 

    LOG_CHANNEL_ID=Text channel ID for logging purposes
    PUNISHMENT_CHANNEL_ID=Text channel ID for logging punishments
    BOTSETUP_CHANNEL_ID=Text channel ID where bot commands/bot setup is done 
    MEMBERCOUNT_CHANNEL_ID=A channel used to update member counts
    IDENTIFY_CHANNEL_ID=Text channel that is used to house non-identified members to remind them to idenitfy themselves
