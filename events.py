# Import thư viện

import discord

# Sự kiện
@client.event

# Tạo phản hồi đơn giản
async def respond(message):
  if message.author == client.user:
    return

contents = message.content.lower()

response = {
  "hi":"f{message.author.mention} konnichiwa~!

  # Thêm các phản hồi

}

reply = response.get(content)
if reply:
  await message.channel.send(reply)

respond()
