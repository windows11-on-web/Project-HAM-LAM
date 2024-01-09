### Project HAM LAM / Gemini
## A community-driven project for databases, dummy data, APIs, AI, DNS, Write blocks, and more

⚠ Warning | DNS has been not coded yet due to limits with duckdns and NoIP and its a pain in the balls

This Project uses the following pre-built projects made by windows11-on-web, More are gonna be added
- Kersonal Database [Dummy data]
- Mandata EVA [Database localhost]

Custom Made tools
- Writerblock [With text based GUI]
- Status [With text based GUI]
- Bots [Yes we added discord mod along with chatbot]
- Starter [Starts the discord bots and Databases]

Deploy [Discord bots, database]
- Git this repo
- Cd to path

```cd Project-HAM-LAM```

- Now go to gemini bots folder and edit discord-bot-mod.py and edit the following line with your discord bot token

```bot_token = os.getenv("YOUR_BOT_TOKEN")```

- and then edit the .env for the chatbot and same just put the token
- Go to the root of the folder Then enter this to your cmd

```pip3 install -r packages.txt && python start.py```

- Now you're done

How to Start an GUI App [Writerblock and Status]
- Cd to their paths [they are in other folders]
- and then 
```python main.py```  
- Now you have started a gui app [Note: to exit one of those apps Do Ctrl + C]
