# this bot scares me

# imports
from dotenv import load_dotenv
from os import getenv
from discord import Embed, Client
from emoji import demojize
from random import choice

# fetch env vars
load_dotenv()
TOKEN = getenv('TOKEN')

# create bot
bot = Client()

# log startup
@bot.event
async def on_ready():
    print("Connected to Discord!")

# on message
@bot.event
async def on_message(ctx):
    # remove all emojies
    scrubbed = demojize(ctx.content)
    # if there exists emoji, fact
    if scrubbed != ctx.content:
        # open and parse files
        with open("facts.txt", "r") as file:
            facts = file.read().split('|')
        with open("quips.txt", "r") as file:
            quips = file.read().split('|')
        # pick fact and quip
        fact = choice(facts)
        quip = choice(quips)
        # stylize fact
        embed = Embed(
            title="A fun fact about the Emoji Movie\u2122!",
            description=f"{fact}\n\n{quip}",
            color=0xffde34
        )
        await ctx.channel.send(embed=embed)
        # log
        try:
            print(f'Sent {fact} to {ctx.channel.name} on {ctx.guild.name}')
        except AttributeError:
            print(f'Sent {fact} to {ctx.author} over Direct Messages')
        

# execute bot code
if __name__ == "__main__":
    bot.run(TOKEN)
