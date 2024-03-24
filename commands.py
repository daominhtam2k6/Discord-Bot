# Import thư viện discord.ext

import discord
from discord.ext import commands

# Tạo một lệnh đơn giản
@commands.slash_command(name = "kiss", decription = "emuach")
async def kiss(ctx, member: discord.Member = None):
  if not member:
    member = ctx.author
    await ctx.reply("Hu?")
    return
    
    kissing = f"{ctx.author.mention} kisses {member.mention}"
    link = "https://i.gifer.com/XJis.gif"
    embed = discord.Embed()
    embed.set_image(url = link)
    await ctx.reply(kissing, embed = embed)
    
