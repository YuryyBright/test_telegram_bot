from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("1839637938:AAF98ldmpcUlP14K3pVz2FJCDEOLpcrkkds")  # Забираем значение типа str
ADMINS = env.list("412034942")  # Тут у нас будет список из админов
IP = env.str("192.168.43.118")  # Тоже str", но для айпи адреса хоста
