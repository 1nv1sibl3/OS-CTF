import os
import discord
from dotenv import load_dotenv
import random
import time

# Load environment variables from a .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Set up the intents
intents = discord.Intents.default()
intents.message_content = True

# Create an instance of a Client with the specified intents
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # Fetch the guild and store it in the client object
    for guild in client.guilds:
        if guild.name == GUILD:
            client.guild = guild
            break

    print(
        f'\n{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        f'{client.user} has connected to Discord!'
    )
    
@client.event
async def on_member_join(member):
    await member.send(f"Welcome to my server! Chat `$help` on my server to start talking with your dear friend {client.user.mention}")
    time.sleep(1)
    await member.send(f"Please invite everyone to join this server to chat with your dear friend: https://discord.gg/4bJkJKvkx2")

@client.event
async def on_message(message):
    if message.guild and message.guild.id == 1253202322440454174:
    
        if message.content.startswith('$'):
            
            #help command   
            if message.content == '$help':
                if message.channel.name == message.author.name:
                    await message.channel.send("Help: \n`$help`: show this message \n `$gif`: send a gif \n `$secret`: send the secret (if you have permission) \n `$msg`: send a message to shikanoko")
                else:
                    await message.channel.send('Help: \n`$help`: show this message \n `$chat`: create private conversation with your dear friend')
            
            #chat command
            elif message.content == '$chat':
                if message.author != client.user:
                    # Create a text channel with the user's name in the guild
                    channel_name = f"{message.author.name}"
                    existing_channel = discord.utils.get(client.guild.channels, name=channel_name)
                    
                    if not existing_channel:
                        overwrites = {
                            client.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                            message.author: discord.PermissionOverwrite(read_messages=True),
                            client.user: discord.PermissionOverwrite(read_messages=True)
                        }
                        new_channel = await client.guild.create_text_channel(channel_name, overwrites=overwrites)
                        await new_channel.edit(topic=f'Private chat with {message.author.name}')
                        await new_channel.edit(slowmode_delay=3)
                        await new_channel.send(f'Welcome to your private chat with your dear friend, {message.author.mention}!')
                    else:
                        await existing_channel.send(f'Your dear friend is already in {existing_channel.mention}, dear {message.author.mention}!')
                
            
            #gif command
            elif message.content.startswith('$gif'):
                if message.channel.name == message.author.name or message.channel.name == 'bot':
                    general_channel = discord.utils.get(client.guild.channels, name='general')
                    random_number = random.randint(1, 3)
                    with open (f'./{random_number}.gif', 'rb') as file:
                        picture = discord.File(file)
                        await general_channel.send(f'Here\'s a gif for everyone from your dear {message.author.mention}! \n ||Part 1: OSCTF{{||', file=picture)
            
            #secret command
            elif message.content.startswith('$secret'):
                if message.channel.name == message.author.name and message.author != client.user:
                    with open ('./secret_fake.gif', 'rb') as file:
                        picture = discord.File(file)
                        await message.channel.send(f'Here is {client.user.mention} secret.! {message.author.mention} please don\'t ask me more', file=picture)
                        time.sleep(5)
                        await message.channel.edit(topic=f'Private chat with {message.author.name} ||Part 4:K0sH1T4nT4n||')
                        
                        
                            
            #msg command
            elif message.content.startswith('$msg'):
                if message.channel.name == message.author.name:
                    botchannel = discord.utils.get(client.guild.channels, name='bot')
                    msgContent = message.content[5:]
                    if msgContent == '':
                        await message.channel.send('Please provide a message to send to your dear friend.')
                    elif msgContent.startswith('$secret'):
                        msg = msgContent[8:]
                        if msg.startswith('$gif'):
                            await message.author.send(f'Here is {client.user.mention} secret:')
                            await message.channel.send(f'Your dear friend recived your message!')
                            with open ('./part3.gif', 'rb') as file:
                                picture = discord.File(file)
                                await message.author.send(file=picture)
                            random_number = random.randint(1, 3)
                            general_channel = discord.utils.get(client.guild.channels, name='general')
                            with open (f'./{random_number}.gif', 'rb') as file:
                                picture = discord.File(file)
                                await general_channel.send(f'Here\'s a gif for everyone from your dear {message.author.mention}! \n ||Part 1: OSCTF{{||', file=picture)                            
                        else:
                            await message.channel.send(f'Your dear friend don\'t have any [text](https://part2.Sh1k4N0k0_) secret for you to show off!')

                            
                        
                    else:
                        await botchannel.send(f'{msgContent} {message.author}')
                        await message.channel.send(f'Your dear friend recived your message!')
        elif message.content != '':
            if message.channel.name == 'general' and  message.author != client.user:
                if message.content !='$chat' and message.content  != '$help':
                    await message.delete()
                    await message.author.send(f"Please send everything in your private channel or else your dear friend {client.user.mention} will be sad :(")
            
# Run the client using the token
client.run(TOKEN)

