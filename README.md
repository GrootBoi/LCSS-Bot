# LCSS-Bot: Jasper
This is the bot for the LCSS Discord server, which uses Python.
Uhh, yeah this is what exists so far, feel free to dig into it if you feel!

# Dependencies
* discord.py 
* python-dotenv
* pymongo
* pymongo[srv]
* pytz

# Getting Started
* A `.env` file is required in the project's root directory with the following fields assigned
```
DISCORD_TOKEN=Insert bot's token
MONGODB_URL=Mongodb DB connection url
```

* Modify the `config.json` file to match your server's channels and edit any bot config

* The program's entry point is `jasper.py` which can be run in a terminal instance using `py jasper.py` 