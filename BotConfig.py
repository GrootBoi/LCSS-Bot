import json
f = open('config.json')
config = json.load(f)

class BotConfig:
    @staticmethod
    def prefix() -> str:
        return config["bot"]["prefix"]

    @staticmethod
    def serverID() -> int:
        return config["server"]["id"]

    @staticmethod
    def channel_log() -> int:
        return config["server"]["channels"]["log"]

    @staticmethod
    def channel_punishment() -> int:
        return config["server"]["channels"]["punishment"]

    @staticmethod
    def channel_botsetup() -> int:
        return config["server"]["channels"]["botsetup"]

    @staticmethod
    def channel_identify() -> int:
        return config["server"]["channels"]["identify"]

    @staticmethod
    def channel_membercount() -> int:
        return config["server"]["channels"]["membercount"]

    @staticmethod
    def channel_general() -> int:
        return config["server"]["channels"]["general"]

    @staticmethod
    def channel_welcome() -> int:
        return config["server"]["channels"]["welcome"]

    @staticmethod
    def embedColor() -> int:
        #embedColor is assumed to be a hex digit, and as such, is converted to base 16
        return int(config["bot"]["embedColor"], 16)


