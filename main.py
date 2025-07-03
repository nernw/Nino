# main.py - Phiên bản cập nhật

import discord, os, asyncio
from discord.ext import commands
from keep_alive import keep_alive # Giữ nguyên dòng này

# Cài đặt Intents
intents = discord.Intents.default()
intents.message_content = True

# Khởi tạo bot
bot = commands.Bot(
    command_prefix="n",
    intents=intents
)

# Sử dụng setup_hook để load các extensions (cogs)
# Đây là cách làm được khuyến nghị, nó sẽ chạy trước khi bot đăng nhập
@bot.event
async def on_ready():
    print(f'Bot đã đăng nhập với tên {bot.user}')
    print(f'ID của bot: {bot.user.id}')
    print('-------------------')
    
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    # Load các cogs trước
    await load_extensions()
    
    # Bật máy chủ keep_alive
    keep_alive()
    
    # Lấy token và chạy bot
    token = os.getenv("DISCORD_TOKEN")
    if token:
        await bot.start(token)
    else:
        print("Lỗi: Biến môi trường DISCORD_TOKEN chưa được thiết lập.")

# Chạy hàm main bằng asyncio
if __name__ == "__main__":
    asyncio.run(main())
