# Import các thư viện cần thiết

import discord
import os
from start import on_ready
import events
from keep_alive import keep_alive

# Khởi tạo bot/client với các intenst

intents = discord.Intents.all()  # Cấp cho bot toàn bộ quyền 
client = discord.Client(intents = intents)  

# Truy cập token bot
TOKEN = os.environ.get('TOKEN')
# >> Tạo một biến môi trường lưu token của bot để đảm bảo về bảo mật <<
# Có thể dùng token trực tiếp: TOKEN = 'YOUR_BOT_TOKEN'

# Chạy bot
client.run(TOKEN)
