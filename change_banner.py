# Import aiohttp và requests

import aiohttp
import requests

# Hàm thay đổi biểu ngữ
async def change_banner():
    url = 'YOUR_BANNER_LINK'
    response = requests.get(url)
    image_data = response.content

    image_base64 = discord.utils._bytes_to_base64_data(image_data)

    payload = {'banner': image_base64}

    async with aiohttp.ClientSession() as session:
        async with session.patch('https://discord.com/api/v9/users/@me', headers={'Authorization': f'Bot {TOKEN}'}, json=payload) as response:
            if response.status == 200:
                print('Banner was updated!')
            else:
                print(f'Errors : {response.status}')

change_banner()
