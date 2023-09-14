from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili


# BOT_TOKEN="6390894534:AAFdiLCCpB66exE_iIQ9fk9tjuKjo2U1fLo"
# ADMINS="6272309525"
