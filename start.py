# Import thư viện

import discord

# Tạo sự kiện khi chạy bot

@client.event
async def on_ready():  # Hàm được gọi khi bot chạy lần đầu

  # Thay đổi trạng thái của bot
  
  await client.change_presence(
    activity = discord.Game(name = 'TRANG_THAI_CUA_BOT')
  )

  # Các sự kiện khác

  await change_banner()  
