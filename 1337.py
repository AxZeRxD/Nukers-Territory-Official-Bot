import discord
from discord.ext import commands
import random
import discord, time, random,json, os
from discord.ext import commands, tasks
import asyncio
import datetime
import re
import os
import json
from itertools import cycle
import jishaku  
import re
from typing import Union
from discord.ext import commands, tasks

intents = discord.Intents.all()

idk = ["-", ""]

def is_owner(ctx):
    return ctx.author.id in owner_id

os.system("cls")
def get_prefix(client, message):
    with open("info.json", "r") as ok:
        try:
            kk = json.load(ok)
            ded = str(kk["np"]) 
            if str(message.author.id) in ded:
                return idk
            else:
                return "-"
        except (json.decoder.JSONDecodeError, KeyError):
            return "-"


def whitelistt(ctx):
  with open('wl.txt', 'r') as file:
    wl = [line.strip() for line in file.readlines()]

client = commands.Bot(command_prefix=get_prefix,
                      intents=discord.Intents.all(),
                      owner_ids=[1181514638106574941,1103331364503289856,1086567184920227900],
                      case_insensitive=True,
                      strip_after_prefix=True)

owner_id = [""] 



@client.event
async def on_ready():
    print("Success: Bot Is Connected To Discord")
    print("Loaded & Online!")
    print(f"Connected to: {len(client.users)} users")
    loda.start()
    
    tci = 1213768911313575957
    tc = client.get_channel(tci)
    if tc:
        voice_channel = await tc.connect()
        await voice_channel.guild.change_voice_state(channel=tc, self_deaf=True)
        client.load_extension("jishaku")


lundlele = cycle(["Nukers Territory™ <$", "Ping: {:.2f} ms"])  

@tasks.loop(seconds=7)
async def loda():
    status_message = next(lundlele)
    if "{:.2f}" in status_message:
        status_message = status_message.format(client.latency * 100)  

    await client.change_presence(activity=discord.Game(name=status_message), status=discord.Status.dnd)
    


def is_aizer(ctx):
  return ctx.author.id == 1103331364503289856


def is_permitted(ctx):
  with open('perms.txt', 'r') as file:
    permitted_users = [line.strip() for line in file.readlines()]
  return str(ctx.author.id) in permitted_users

        

tick = "<:stolen_emoji:1188884329238106193>"
cross = "<:stolen_emoji:1188884392404340737>"
clr = discord.Colour.default()

client.remove_command("help")
 





@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Nukers Territory",
        description=f"Hy {ctx.author.mention}",
        color=discord.Color.blue()
    )

    embed.add_field(name="Fun", value="`wizz`", inline=False)
    embed.add_field(name="Moderation", value="`ban`,`kick`,`unban`,`lock`,`unlock`,`hide`,`unhide`", inline=False)
    embed.add_field(name="Role", value="`staff`,`rstaff`,`buddy`,`rbuddy`,`qt`,`rqt`", inline=False)

    embed.set_footer(text="discord.gg/ntop")
    
    await ctx.send(embed=embed)


@client.command()
async def wizz(ctx):
  x = await ctx.send(
    f"`Wizzing {ctx.guild.name}, will take 69 seconds to complete`")
  z = await ctx.send(f"`successfully pruned {ctx.guild.name}`")
  e = await ctx.send("`Deleting Channels...`")
  r = await ctx.send("`Deleting roles...`")
  t = await ctx.send("`Installing Ban Wave..`")
  time.sleep(0)
  await x.delete()
  await z.delete()
  await e.delete()
  await r.delete()
  await t.delete()
  await ctx.send(f"**{tick} `successfully wizzed {ctx.guild.name}`**")



@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: Union[discord.Member, int] = None, *, reason=None):
    if not (ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
        embed = discord.Embed(
            title=f"{ctx.author.name}",
            description=f"{cross} | Your top role should be above my top role",
            color=clr)
        await ctx.send(embed=embed)
    elif member is None:
        embed = discord.Embed(
            title=f"{ctx.author.name}",
            description=f"{cross} | Please provide a valid member or user ID to ban",
            color=clr)
        await ctx.send(embed=embed)
    else:
        guild = ctx.guild
        if isinstance(member, discord.Member):
            member_id = member.id
        elif isinstance(member, int):
            member_id = member
        else:
            return

        member_to_ban = guild.get_member(member_id)

        if member_to_ban:
            await guild.ban(member_to_ban, reason=f"Banned by {ctx.author.name} | {reason}")

            try:
                ban_reason = f"❗You have been banned from **`{guild.name}`**.\nReason: **`{reason}`**\nResponsible Moderator: **`{ctx.author.name}`**"
                await member_to_ban.send(ban_reason)
            except discord.errors.Forbidden:
                pass  

            embed = discord.Embed(
                title=f"{ctx.author.name}",
                description=f"{tick} | Successfully banned {member_to_ban.name}",
                color=clr)
            embed.set_footer(text=f"Reason: {reason} | Nukers Territory™")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f"{ctx.author.name}",
                description=f"{cross} | Member not found",
                color=clr)
            await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if not (ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
        embed = discord.Embed(
            title=f"{ctx.author.name}",
            description=f"{cross} | Your top role should be above my top role",
            color=clr)
        await ctx.send(embed=embed)
    else:
        guild = ctx.guild
        await guild.kick(member, reason=f"Kicked by {ctx.author.name} | {reason}")

        try:
            kick_reason = f"❗You have been kicked from **`{guild.name}`**.\nReason: **`{reason}`**\nResponsible Moderator: **`{ctx.author.name}`**"
            await member.send(kick_reason)
        except discord.errors.Forbidden:
            pass  

        embed = discord.Embed(
            title=f"{ctx.author.name}",
            description=f"**{member.name}** has been kicked",
            color=clr)
        embed.set_footer(text=f"Reason: {reason} | Nukers Territory™")
        await ctx.send(embed=embed)


#@commands.has_permissions(manage_channels=True)
@client.command()
@commands.has_permissions(administrator=True)
async def lock(ctx, channel: discord.TextChannel = None):
  if not (ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
    embed = discord.Embed(
      title=f"{ctx.author.name}",
      description=f"{cross} | Your top role should be above my top role",
      color=clr)
    await ctx.send(embed=embed)
  else:
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(
      title="",
      description=f"{tick} | {channel.mention} has been locked",
      color=clr)
    embed.set_footer(text="Nukers Territory™")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def unlock(ctx, channel: discord.TextChannel = None):
  if not (ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
    embed = discord.Embed(
      title=f"{ctx.author.name}",
      description=f"{cross} | Your top role should be above my top role",
      color=clr)
    await ctx.send(embed=embed)
  else:
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(
      title="",
      description=f"{tick} | {channel.mention} has been unlocked",
      color=clr)
    embed.set_footer(text="Nukers Territory™")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def hide(ctx, channel: discord.TextChannel = None):
  if not (ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
    embed = discord.Embed(
      title=f"{ctx.author.name}",
      description=f"{cross} | Your top role should be above my top role",
      color=clr)
    await ctx.send(embed=embed)
  else:
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(
      title="",
      description=f"{tick} | {channel.mention} is now hidden",
      color=clr)
    embed.set_footer(text="Nukers Territory™")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def unhide(ctx, channel: discord.TextChannel = None):
  if not (ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
    embed = discord.Embed(
      title=f"{ctx.author.name}",
      description=f"{cross} | Your top role should be above my top role",
      color=clr)
    await ctx.send(embed=embed)
  else:
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(
      title="",
      description=f"{tick} | {channel.mention} is now visible",
      color=clr)
    embed.set_footer(text="Nukers Territory™")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.send(embed=embed)

@client.command(
    name="unban",
    help="If someone realizes his mistake you should unban him",
    usage="unban [user]")
@commands.has_permissions(ban_members=True)
async def unban(ctx: commands.Context, id: int):
    if not ctx.author.top_role.position > ctx.guild.me.top_role.position:
        embed = discord.Embed(
            title=f"{ctx.author.name}",
            description=f"{cross} | Your top role should be above my top role",
            color=clr)
        await ctx.send(embed=embed)
        return

    try:
        user = await client.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed(
            color=clr,
            description=f"{tick} | {user.name} has been successfully unbanned",
            timestamp=ctx.message.created_at)
        embed.set_author(name=f"{ctx.author.name}")
        await ctx.send(embed=embed)
    except discord.NotFound:
        embed = discord.Embed(
            color=clr,
            description=f"{cross} | User not found or not banned",
            timestamp=ctx.message.created_at)
        embed.set_author(name=f"{ctx.author.name}")
        await ctx.send(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(
            color=clr,
            description=f"{cross} | I don't have permission to unban",
            timestamp=ctx.message.created_at)
        embed.set_author(name=f"{ctx.author.name}")
        await ctx.send(embed=embed)




@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, amount: int):
  await ctx.channel.purge(limit=amount)
  m = await ctx.send(f"{tick} | successfully purged {amount} message")
  await ctx.message.delete()
  await m.delete()

    
q = client.get_channel(1213746355319734313)
w = "<@1103331364503289856> <@1141039842348777623> <@1103331364503289856>"

guild = client.get_guild(1099703918298136718)


@client.event
async def on_webhooks_update(channel):
    guild = channel.guild
    if guild.id != 1099703918298136718:
        return

    mohit = client.get_channel(1213746355319734313)

    async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_create):
        user_id = entry.user.id

        try:
            with open('wl.txt', 'r') as file:
                wl = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            wl = []

        if user_id in wl:
            print("IDK")
        else:
            try:
                await guild.ban(entry.user, reason="ANTIWEBHOOK CREATE | AIZER")
            except discord.Forbidden:
                pass

        webhooks = await guild.webhooks()
        for webhook in webhooks:
            await webhook.delete()

        if mohit:
            embed = discord.Embed(
                title="Webhook Creation",
                description="Someone attempted to create a webhook.",
                color=clr
            )
            embed.add_field(name="Guild", value=guild.name)
            embed.add_field(name="Channel", value=channel.name)
            embed.add_field(name="User", value=entry.user.mention)
            embed.set_footer(text=f"User ID: {user_id}")

            await mohit.send(embed=embed)




@client.event
async def on_command_completion(ctx):
    command = ctx.command
    user = ctx.author

    i = f"Command '{command.name}' triggered by '{user.name}'"
    command.request_count = getattr(command, 'request_count', 0) + 1

    embed = discord.Embed(
        title="Command Triggered",
        description=i,
        color=clr
    )
    embed.add_field(name="Command", value=command.name)
    embed.add_field(name="User", value=user.name)
    embed.add_field(name="Request Count", value=command.request_count)

    channel_id = 1213746355319734313 
    channel = client.get_channel(channel_id)

    if channel:
        await channel.send(embed=embed)




@client.group(name="np", invoke_without_command=True)
@commands.check(is_owner)
async def np(ctx: commands.Context):
  if ctx.subcommand_passed is None:
    await ctx.send_help(ctx.command)
    ctx.command.reset_cooldown(ctx)
    

@np.command()
@commands.is_owner()
async def add(ctx, user: discord.Member):
  try:
    with open('info.json', 'r') as idk:
      data = json.load(idk)
      np = data["np"]

    if user.id in np:
      embed = discord.Embed(
          description=
          f"{cross} | {user.name} already has no prefix",
          color=discord.Colour.default())
      await ctx.send(embed=embed)
    else:
      data["np"].append(user.id)
      with open('info.json', 'w') as idk:
        json.dump(data, idk, indent=4)
      embed = discord.Embed(
          description=
          f"{tick} | Added no prefix to {user.name}",
          color=discord.Colour.default())
      await ctx.send(embed=embed)

  except Exception as e:
    embed = discord.Embed(description=f"An error occurred: {e}",
                          color=discord.Colour.default())
    await ctx.send(embed=embed)


@np.command()
@commands.is_owner()
async def remove(ctx, user: discord.Member):
  try:
    with open('info.json', 'r') as idk:
      data = json.load(idk)
      np = data["np"]

    if user.id in np:
      data["np"].remove(user.id)
      with open('info.json', 'w') as idk:
        json.dump(data, idk, indent=4)
      embed = discord.Embed(
          description=
          f"{tick} | Removed no prefix from {user.name}",
          color=discord.Colour.default())
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(
          description=
          "{cross} | This user does not have no prefix!",
          color=discord.Colour.default())
      await ctx.send(embed=embed)

  except Exception as e:
    embed = discord.Embed(description=f"An error occurred: {e}",
                          color=discord.Colour.default())
    await ctx.send(embed=embed)



@client.event
async def on_member_join(member):
    roles_to_add = [1213753501868621844, 1213599363574792222]
    for role_id in roles_to_add:
        role = discord.utils.get(member.guild.roles, id=role_id)
        if role:
            await member.add_roles(role, reason="Nukers Territory™ | AUTOROLE")

            

@client.command(name="ap")
@commands.is_owner()
async def add_perms(ctx, target_user: discord.Member):
  try:
    with open('perms.txt', 'r') as file:
      lines = file.readlines()

    target_user_id = str(target_user.id)

    if target_user_id in lines:
      embed = discord.Embed(
          title="Error",
          description=
          f"{cross} | {target_user.mention}'s ID is already in the Data Base.",
          color=discord.Colour.default())
      await ctx.send(embed=embed)
      return

    with open('perms.txt', 'a') as file:
      file.write(f"{target_user_id}\n")

    embed = discord.Embed(
        title="Permissions Added",
        description=
        f"{tick} | Added permissions to {target_user.mention}.",
        color=0x00FF00)
    await ctx.send(embed=embed)

  except Exception as e:
    embed = discord.Embed(title="Error",
                          description=f"An error occurred: {e}",
                          color=discord.Colour.default())
    await ctx.send(embed=embed)


@client.command(name="rp")
@commands.is_owner()
async def remove_perms(ctx, target_user: discord.Member):
  try:
    with open('perms.txt', 'r') as file:
      lines = file.readlines()

    target_user_id = str(target_user.id)

    if target_user_id not in lines:
      embed = discord.Embed(
          title="Error",
          description=
          f"{cross} | {target_user.mention}'s ID is not found in the Data Base.",
          color=0x000000)
      await ctx.send(embed=embed)
      return

    with open('perms.txt', 'w') as file:
      for line in lines:
        if line.strip() != target_user_id:
          file.write(line)

    embed = discord.Embed(
        title="Permissions Removed",
        description=
        f"{tick} | Removed permissions from {target_user.mention}.",
        color=0x000000)
    await ctx.send(embed=embed)

  except Exception as e:
    embed = discord.Embed(title="Error",
                          description=f"An error occurred: {e}",
                          color=0x000000)
    await ctx.send(embed=embed)


@client.command()
@commands.check(is_permitted)
@commands.has_permissions(administrator=True)
async def buddy(ctx, member: discord.Member):
    try:
        buddy = 1213764069291720704
        buddyrole = ctx.guild.get_role(buddy)
        if buddyrole:
            await member.add_roles(buddyrole , reason=f"Command Used By : {ctx.author}")
            embed = discord.Embed(
                title="BUDDY ROLE",
                description=f"{tick} | Successful Add {buddyrole.mention} To {member.mention}.",
                color=0x000000
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{cross} | The Buddy role does not exist on this server.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        

@client.command()
@commands.check(is_permitted)
@commands.has_permissions(administrator=True)
async def staff(ctx, member: discord.Member):
    try:
        staff = 1213762834991939584
        staffrole = ctx.guild.get_role(staff)
        if staffrole:
            await member.add_roles(staffrole , reason=f"Command Used By : {ctx.author}")
            embed = discord.Embed(
                title="STAFF ROLE",
                description=f"{tick} | Successful Add {staffrole.mention} To {member.mention}.",
                color=0x000000
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{cross} | The admin role does not exist on this server.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        
@client.command()
@commands.check(is_permitted)
@commands.has_permissions(administrator=True)
async def qt(ctx, member: discord.Member):
    try:
        qt = 1213763924718125056
        qtrole = ctx.guild.get_role(qt)
        if qtrole:
            await member.add_roles(qtrole , reason=f"Command Used By : {ctx.author}")
            embed = discord.Embed(
                title="QTZ ROLE",
                description=f"{tick} | Successful Add {qtrole.mention} To {member.mention}.",
                color=0x000000
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{cross} | The qtz role does not exist on this server.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        
        
@client.command()
@commands.check(is_permitted)
@commands.has_permissions(administrator=True)
async def rbuddy(ctx, member: discord.Member):
    try:
        buddy = 1213764069291720704
        buddyrole = ctx.guild.get_role(buddy)
        if buddyrole and buddyrole in member.roles:
            await member.remove_roles(buddyrole, reason=f"Command Used By: {ctx.author}")
            embed = discord.Embed(
                title="BUDDY ROLE",
                description=f"{tick} | Successfully removed {buddyrole.mention} from {member.mention}.",
                color=0x000000
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{cross} | {member.mention} does not have the Buddy role.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@client.command()
@commands.check(is_permitted)
@commands.has_permissions(administrator=True)
async def rstaff(ctx, member: discord.Member):
    try:
        staff = 1213762834991939584
        staffrole = ctx.guild.get_role(staff)
        if staffrole and staffrole in member.roles:
            await member.remove_roles(staffrole, reason=f"Command Used By: {ctx.author}")
            embed = discord.Embed(
                title="STAFF ROLE",
                description=f"{tick} | Successfully removed {staffrole.mention} from {member.mention}.",
                color=0x000000
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{cross} | {member.mention} does not have the Staff role.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@client.command()
@commands.check(is_permitted)
@commands.has_permissions(administrator=True)
async def rqt(ctx, member: discord.Member):
    try:
        qt = 1213763924718125056
        qtrole = ctx.guild.get_role(qt)
        if qtrole and qtrole in member.roles:
            await member.remove_roles(qtrole, reason=f"Command Used By: {ctx.author}")
            embed = discord.Embed(
                title="QTZ ROLE",
                description=f"{tick} | Successfully removed {qtrole.mention} from {member.mention}.",
                color=0x000000
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{cross} | {member.mention} does not have the QTZ role.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

        


client.run("")