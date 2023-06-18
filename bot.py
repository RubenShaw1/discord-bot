#!/usr/bin/python
import discord
from discord.ext import commands
import requests
import os

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

token = os.environ['TOKEN']

@bot.event
async def on_ready():
    print(f'Im ready! Logged in as {bot.user.name}')


@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'Welcome, {member.mention}.')


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f'{member.mention} has been kicked.')


@bot.command()
@commands.has_role('Owner')
async def announce(ctx, *, announcement: str):
    author = ctx.message.author
    await ctx.send(f'{author.name} wants everyone to know that {announcement}')



bot.run(token)
