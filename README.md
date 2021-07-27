# HuskyBot
A Discord bot for the Northeastern '24 server. 

## Features

* Private message a bot and have it output your message into a separate channel (anonymously)!
* Alternatively, use the command directly in a Discord channel the bot has access to.

* Picture support (upload the image onto Discord)
* Embed styling (includes text, picture, and time/date)
* Keyword detection (to prevent malicious messages)
* Multiple channel support
* Help command

## Screenshots

**Example Private Message**

![Private Message the Bot](pictures/botPM.png)


**Example Output**

![Output](pictures/botOutput.png)


**Example Help Command**

![Help Command](pictures/botHelp.png)

**Example Invalid Command**

![Failed Message](pictures/botInvalidMessage.png)

## Running
    # For the host:
    python bot.py

    # For the user:
    Private message a bot: !conf (message)
    Message in a channel the bot can see: !conf(message)
    (Attach a picture using Discord's upload system)

## Things the User Must Do
Before running the bot, add the following IDs in the bot.py file (at the top):
* Guild/Server ID (int)
* Channel ID (int)
* Bot Token ID (string)

## Requirements
Requires Python, discord.py and NodeJS.

## Installing discord.py
    # Linux/macOS
    python3 -m pip install -U discord.py

    # Windows
    py -3 -m pip install -U discord.py