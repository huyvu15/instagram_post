# from instabot import Bot

# # photo = "soaps.jpg"

# bot = Bot()

# # bot.api.cookie_jar.clear()


# bot.login(username = 'pudaide', password = '382003')

# bot.upload_photo("resized.jpg", caption = "The soaps cover by blue sky")
from instabot import Bot

# Tạo một đối tượng Bot
bot = Bot()

# Đăng nhập vào tài khoản Instagram
bot.login(username='pudaide', password='382003')

# Đăng ảnh lên Instagram
caption = "Mô tả ảnh của bạn ở đây"
image_path = "with_Tep.jpg"  # Đường dẫn đến tệp ảnh bạn muốn đăng

bot.upload_photo(image_path, caption=caption)

# Đăng xuất sau khi hoàn thành
bot.logout()
