from Bard import Chatbot
import discord
from discord import option
from discord.ext import commands #import neccessary modules
from dotenv import load_dotenv
import os
import random

load_dotenv() #load environment
discord_token=os.environ["DISCORD_TOKEN"]
bard_token=os.environ["BARD_TOKEN"] 

bot = commands.Bot(command_prefix="bard.", intents=discord.Intents.all(), help_command=None) #create bot
chatbot = Chatbot(bard_token) #create bard client

@bot.event
async def on_ready():
    print("Bard is ready for use!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.mentions:
        for mention in message.mentions:
            if mention.id == bot.user.id: #checking for mention of bot in messages
                msg = await message.reply("Bard is thinking...")
                answer = chatbot.ask(message.content.replace(bot.user.mention, "")) #get answer
                if len(answer['content']) > 2000: #if output will be > 2000 characters it will be sent as file because of Discord restrictions
                    i = random.randint(1, 10000000)
                    with open(f"{i}.txt", "w") as f:
                        f.write(answer['content'])
                    await msg.edit(file=discord.File(f"{i}.txt"))
                else:
                    await msg.edit(content=answer['content'])   
                    
bot.run(discord_token) #run bot
