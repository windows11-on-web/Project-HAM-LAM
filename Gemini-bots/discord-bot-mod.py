# Print that it is started
print("Discord bot mod module has been started, Running v1.0")

import discord
from discord.ext import commands
import os

# Replace with your actual bot token
bot_token = os.getenv("YOUR_BOT_TOKEN")

# Initialize the bot
bot = commands.Bot(command_prefix=">mod")

# Define a function to check if the user is a moderator
def is_moderator(ctx):
    return ctx.message.author.guild_permissions.administrator or ctx.message.author.id in bot.owner_ids

# Kick command
@bot.command(name="kick", require_permissions=is_moderator)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"User {member} has been kicked.")

# Ban command
@bot.command(name="ban", require_permissions=is_moderator)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"User {member} has been banned.")

# Mute command
@bot.command(name="mute", require_permissions=is_moderator)
async def mute(ctx, member: discord.Member, *, reason=None):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        await ctx.send("Muted role doesn't exist. Please create one first.")
        return
    await member.add_roles(muted_role)
    await ctx.send(f"User {member} has been muted.")

# Unmute command
@bot.command(name="unmute", require_permissions=is_moderator)
async def unmute(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(muted_role)
    await ctx.send(f"User {member} has been unmuted.")

# Clear messages command
@bot.command(name="clear", require_permissions=is_moderator)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Cleared {amount} messages.")

# User info command
@bot.command(name="userinfo", aliases=["user", "info"])
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title=f"User information for {member.name}", color=0x00ff00)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Name", value=member.name)
    embed.add_field(name="Discriminator", value=member.discriminator)
    embed.add_field(name="Joined at", value=member.joined_at)
    embed.add_field(name="Roles", value=", ".join([role.name for role in member.roles]))
    await ctx.send(embed=embed)

# Server info command
@bot.command(name="serverinfo", aliases=["server"])
async def serverinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name} server information", color=0x00ff00)
    embed.add_field(name="ID", value=ctx.guild.id)
    embed.add_field(name="Name", value=ctx.guild.name)
    embed.add_field(name="Owner", value=ctx.guild.owner)
    embed.add_field(name="Member count", value=ctx.guild.member_count)
    embed.add_field(name="Creation date", value=ctx.guild.created_at)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

# Run the bot
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(bot_
