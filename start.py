print("Gemini v1.0 [Starting Modules]")

import os
from subprocess import Popen

code_root_directory = os.path.dirname(os.path.realpath(__file__))

discord_bots_directory = os.path.join(code_root_directory, "Gemini-bots")
discord_bot_mod_file = os.path.join(discord_bots_directory, "discord-bot-mod.py")
discord_bot_chatbot_file = os.path.join(discord_bots_directory, "discord-bot-chatbot.py")
database_mandb_file = os.path.join(code_root_directory, "Gemini-db", "main.py")
database_dummy_file = os.path.join(code_root_directory, "Gemini-Data", "main.py")

processes = []

process = Popen(["python", discord_bot_mod_file])
processes.append(process)

process = Popen(["python", discord_bot_chatbot_file])
processes.append(process)

process = Popen(["python", database_mandb_file])
processes.append(process)

process = Popen(["python", database_dummy_file])
processes.append(process)

for process in processes:
    process.wait()

print("All the modules have been started")
