from discord.ext import commands
from datetime import datetime
from io import BytesIO
import discord

####################

# Specific information necessary for bot to function
# Obtain guild ID by right-clicking the server and clicking "Copy ID"
GUILD_ID = ID_HERE # Guild ID MUST be an int, not a string!

# Obtain channel ID by right-clicking the channel and clicking "Copy ID"
CHANNEL_ID = ID_HERE #Channel ID MUST be an int, not a string!

# Obtain bot token from Discord Developer Site
BOT_TOKEN = "ID_HERE" # Token ID MUST be a string (in quotes)!

####################

# Creates the instances, uses "!" to activate commands
bot = commands.Bot(command_prefix='!')

# "!conf" command
@bot.command()
async def conf(ctx, *, message=""):

    # Error check: skips if message has no content or image
    if (len(message) != 0) or (ctx.message.attachments != []):

      # Obtains User ID and nickname to verify user is in guild/server
      userID = (ctx.message.author.id)
      server = bot.get_guild(GUILD_ID)
      member = server.get_member(userID)

      # If member is a member of the server, they will have a name (instead of None)
      if member != None:
        # Assigns Discord channel (given channel ID)
        channel = bot.get_channel(CHANNEL_ID)

        # datetime object containing current date and time
        now = datetime.now()
        currentTime = now.strftime("%d/%m %H:%M")

        # Create embed message (looks better)
        embed = discord.Embed(description=message)

        # Set date/time as footer of embed
        embed.set_footer(text=currentTime)

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
        await ctx.send("Your message has been sent!")

      # If member is not a member is the server, they will be tagged None
      else:
        await ctx.send("You are not a member of the server! The message was not sent.")   

    # If the message contains no image or text
    else:
      await ctx.send("Your message does not contain any content. Message failed.")


# Runs the bot given bot token ID
bot.run(BOT_TOKEN)