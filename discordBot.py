import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
TOKEN = os.getenv("TOKEN")

tracker = {
    "aj being too hot": 1000,
    "aj being too cold": 10,
    "alex's dead horses": 3,
    "times dom noticed the new bot": 1,
}


def showOne(msg):
    one = msg.split(">show ", 1)[1]
    try:
        return f"{one} = {tracker[one]}"
    except:
        return "That tracker doesn't exist"


def create(msg):
    newTracker = msg.split(">create ", 1)[1]
    if len(newTracker) == 0:
        return "You didnt give the tracker a name silly"
    if newTracker not in tracker:
        tracker[newTracker] = 1
        return f"New Tracker made, {newTracker} = {tracker[newTracker]}"

    else:
        f"That tracker is already made, {newTracker} = {tracker[newTracker]}"


def add(msg):
    text = msg.split(">add ", 1)[1]
    val = [int(char) for char in text.split() if char.isdigit()][0]
    key = " ".join(text.split(str(val), 1)[0].rsplit())

    try:
        tracker[key] += val
        return f"{key} = {tracker[key]}"
    except:
        return "That Tracker doesn't exist"


def remove(msg):
    text = msg.split(">remove ", 1)[1]
    val = [int(char) for char in text.split() if char.isdigit()][0]
    key = " ".join(text.split(str(val), 1)[0].rsplit())

    try:
        tracker[key] -= val
        return f"{key} = {tracker[key]}"
    except:
        return "That Tracker doesn't exist"


@client.event
async def on_ready():
    print("bot is ready")


@client.event
async def on_message(message):
    msg = message.content
    if msg.startswith(">create"):
        newTracker = create(msg)
        await message.channel.send(newTracker)

    if msg.startswith(">show"):
        singleTracker = showOne(msg)
        await message.channel.send(singleTracker)

    if msg.startswith(">add"):
        total = add(msg)
        await message.channel.send(total)

    if msg.startswith(">remove"):
        total = remove(msg)
        await message.channel.send(total)

    if msg.startswith(">show all"):
        for keys in tracker:
            await message.channel.send(f"{keys} = {tracker[keys]}")


client.run(TOKEN)