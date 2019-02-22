import sys
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random

#Usage: type '!team' and then add all the players you want separated by space. Make sure it is an even amount of players. Player names cannot contain a space. Example:
#!team rookie noob PuCrusher magival man Kaan
#writing that will make the bot shuffle the names around and spit out 2 teams.

client = Bot(description="Random team generator bot By Zyxer", command_prefix="!", pm_help = False)
players = []
@client.command(pass_context=True)
async def team(ctx, *, x):
    players = [y.strip() for y in x.split(' ')]
    random.shuffle(players)
    y = len(players)/2
    msg = "Team 1:\n{}\n\nTeam 2:\n{}".format(players[:int(y)], players[int(y):])
    await client.say(msg)

client.run('token goes here')
