from discord.ext import commands
from datetime import datetime
from io import BytesIO

# If you want to prevent keywords from appearing in a confession, implement SequenceMatcher
# from difflib import SequenceMatcher

import discord

####################

# Specific information necessary for bot to function

# The Guild ID refers to the server the bot will operate in.
# Obtain guild ID by right-clicking the server and clicking "Copy ID"
GUILD_ID = ID_HERE # Guild ID MUST be an int, not a string!

# The Channel ID refers to the specific channel the bot will be able to interact with.
# Obtain channel ID by right-clicking the channel and clicking "Copy ID"
# Channel ID MUST be an int, not a string!

# Examples of possible channels have been listed
CONFESSIONS_ID = ID_HERE # confessions, !conf 
VENT_ID = ID_HERE # vent, !vent
VC_CHAT_ID = ID_HERE # vc-chat, !vc
LGBTQ_ID = ID_HERE # lgbtq, !lgbt
TIKTOK_ID = ID_HERE # tiktoks, !tiktok
MEMES_ID = ID_HERE # ID_HERE, !meme
RECOMMENDATIONS_ID = ID_HERE # recommendations, !rec

# The Bot Token is necessary for the program to interact with the Discord API.
# Obtain bot token from Discord Developer Site
BOT_TOKEN = "ID_HERE" # Token ID MUST be a string (in quotes)!

####################

# # String Sequence Comparison
# a = 'bad phrase here'
# seq = SequenceMatcher()

# Creates the instances, uses "!" to activate commands
bot = commands.Bot(command_prefix='!')

# # sets custom status message / activity
# @bot.event
# async def on_ready():
#     await bot.change_presence(activity=discord.Game(name="!confhelp"))

# "!conf" command
# Aliases are the different names that can be used to invoke a message. The alias used can be retrieved later.
@bot.command(aliases=['vent', 'vc', 'lgbt', 'tiktok', 'meme', 'rec'])
# @bot.command()
async def conf(ctx, *, message=""):

    # Error check: skips if message has no content or image
    if (len(message) != 0) or (ctx.message.attachments != []):

      # # Error check: has "bad phrase"
      # seq.set_seqs(a.lower(), message.lower())
      # if seq.ratio() < 0.66:
      # (need an else case to ignore the command)

        # Assigns Discord channel (given channel ID)
        curAlias = ctx.invoked_with

        # Defaults the channel (to send message to) to the confessions channel
        # TODO: is this necessary?
        channel = bot.get_channel(CONFESSIONS_ID)

        # Checks the alias to see if the user wanted to send the message elsewhere.
        # TODO: can this be simplified?
        if curAlias == 'conf':
          channel = bot.get_channel(CONFESSIONS_ID)
        elif curAlias == 'vent':
          channel = bot.get_channel(VENT_ID)  
        elif curAlias == 'vc':
          channel = bot.get_channel(VC_CHAT_ID)
        elif curAlias == 'lgbt':
          channel = bot.get_channel(LGBTQ_ID)
        elif curAlias == 'tiktok':
          channel = bot.get_channel(TIKTOK_ID)
        elif curAlias == 'meme':
          channel = bot.get_channel(MEMES_ID)
        elif curAlias == 'rec':
          channel = bot.get_channel(RECOMMENDATIONS_ID)
        else:
          channel = bot.get_channel(CONFESSIONS_ID)

        # datetime object containing current date and time
        # the datetime object provides proper time-zone support.
        now = datetime.now()
        currentTime = now.strftime("%m/%d %H:%M")

        # Create embed message (looks better)
        embed = discord.Embed(description=message)

        # Set date/time as footer of embed
        embed.set_footer(text=currentTime + " Ritz's Domain")

        # Image attachments
        files = []
        for file in ctx.message.attachments:
            fp = BytesIO()
            await file.save(fp)
            files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
            imageURL = ctx.message.attachments[0].url
            embed.set_image(url=imageURL)
        # The following prints the image as a separate message
        # await channel.send(files=files)

        # Send embed message to channel
        await channel.send(embed=embed)

        # Inform user their message has been sent
        await ctx.send("Your confession has been sent.")

      # # Has invalid phrase
      # else: 
      #   await ctx.send("Warning: message contains invalid words.") 

    # If the message contains no image or text
    else:
      await ctx.send("Warning: invalid message.")

# "!confhelp" command
@bot.command()
async def confhelp(ctx):
  file = discord.File("loveiswar.gif", filename="loveiswar.gif")

  embed = discord.Embed(title="To use: !(channel) (msg)")
  embed.set_author(name="Anthony Bot (Confessions) - Help")
  embed.set_thumbnail(url="attachment://image here.png") # image goes into content root directory.
  embed.add_field(name="Command", value="!conf\n!vent\n!vc\n!lgbt\n!tiktok\n!meme\n!rec", inline=True) # Table of commands
  embed.add_field(name="Channel", value="[#confessions](link to channel here)", inline=True) # Add links to the channel here
  await ctx.send(file=file, embed=embed)

# Runs the bot given bot token ID
bot.run(BOT_TOKEN)