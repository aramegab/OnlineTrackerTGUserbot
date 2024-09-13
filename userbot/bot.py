from pyrogram import Client, filters
from pyrogram.enums import UserStatus
from pyrogram.errors import FloodWait
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

api_id = config["account"]["api_id"]
api_hash = config["account"]["api_hash"]
user_id = config["account"]["user_id"]
app = Client("userbot", api_id=api_id, api_hash=api_hash)

previous_status = None

def run_status_update():
    app.start()  
    global previous_status
    while True:
        try:
            user = app.get_users(user_id)
            current_status = user.status

            
            if current_status != previous_status:
                if current_status == UserStatus.ONLINE:
                    app.update_profile(last_name='Online🟢')
                else:
                    app.update_profile(last_name='Offline❌')

                previous_status = current_status  

            sleep(10)
        except Exception as e:
            print(f"Error: {e}")
            sleep(10)


run_status_update()
