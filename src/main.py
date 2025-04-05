import discord
from tokenbot import bot_token
from discord.ext import commands  # Imports discord commands

intents = discord.Intents.all() # Creates intents for the bot
client = commands.Bot(command_prefix='!', intents=intents)  # !command to call on command
client.remove_command('help')  # Removes help command so I can use my own

@client.command(pass_context=True, aliases=['intro', 'hi', 'hello', 'h'])  # help commands
async def help(ctx):
    await ctx.send("Hello there! (•◡•) /\n"
                    "I am a bot that converts text into a friendly font!\n"
                    "Use '!friendify (or !f) \\{your message here\\}' to try it out!\n"
                    "Use '!off' to set the bot offline.\n")

@client.event  # Tells me if this is running in the console
async def on_ready():
    print('Bot is online!')

@client.event
async def on_message(message):
    if message.content.startswith('!') and not message.content[1:].split()[0] in client.all_commands:
        await message.channel.send("Sorry! That's not one of my commands! (╯°□°）╯︵ ┻━┻\nYou can see a list of my commands with !help")
    await client.process_commands(message)  # Ensure other commands still work

@client.command(pass_context=True, aliases=['f'])  # Friendify command
async def friendify(ctx, *, message: str):
    if len(message) >= 80:
        await ctx.send("Sorry!! (┳Д┳) Your input message is too long! Please keep it under 80 characters. (>_<)")
        return
    from emoji_id import emoji_ids  # Import emoji_ids from emoji_id.py
    friendified_message = ''.join(
        f"<:{char.lower()}_:{emoji_ids[char.lower() + '_']}>" if char.lower() + '_' in emoji_ids else '    ' if char == ' ' else char
        for char in message
    )
    # user_id = ctx.author.display_name  # Get the user ID of who sent the command
    # await ctx.send(f"{user_id}: {friendified_message}") # shows who sent it
    await ctx.send(friendified_message)

@client.command(pass_context=True) # Kill program - brings bot offline
async def off(ctx):
    await ctx.send("Setting offline! No longer running")
    await client.logout()
    print("Bot is offline!")

client.run(bot_token)