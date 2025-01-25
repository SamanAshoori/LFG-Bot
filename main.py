import discord
import os

# Load the token from Replit Secrets
TOKEN = os.environ.get('DISCORD_TOKEN')

# Check if the token is loaded
if TOKEN is None:
    print("Error: DISCORD_TOKEN not found in environment variables.")
    exit(1)

# List of GIF files to alternate between
GIF_FILES = ['main.gif', 'main2.gif',"main3.gif"]

# Toggle variable to alternate between GIFs
current_gif_index = 0

# Create a Discord client
intents = discord.Intents.default()
intents.message_content = True  # Enable access to message content
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    global current_gif_index  # Use the global variable to track the current GIF

    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message ends with '!!!'
    if message.content.endswith('!!!'):
        # Send the current GIF file
        with open(GIF_FILES[current_gif_index], 'rb') as gif:
            await message.channel.send(file=discord.File(gif))

        # Toggle to the next GIF
        current_gif_index = (current_gif_index + 1) % len(GIF_FILES)

# Run the bot
client.run(TOKEN)
