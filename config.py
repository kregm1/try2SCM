# - *- coding: utf- 8 - *-
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
BOT_TOKEN = config["settings"]["token"]
admins = config["settings"]["admin_id"]
if "," in admins:
    admins = admins.split(",")
else:
    if len(admins) >= 1:
        admins = [admins]
    else:
        admins = []
        print("админ ID?")

bot_version = "0.01"
bot_description = ""
