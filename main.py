# Ну тут все просто UPD (было когда то)
from vkbottle import Bot
from tortoise import Tortoise
import config
from commands import labelers

from middlewares import NoBotMiddleware, RegistrationMiddleware

async def init_tortoise():
    "Подключение к базе из папки data"
    await Tortoise.init(
        db_url='sqlite://data/db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()




bot = Bot(config.main_token)  # Сюда ключ доступа для работы бота

bot.labeler.vbml_ignore_case = True  # пассер сообщений от vkbottle просто потому что удобно
for custom_labeler in labelers:
    """
здесь мы проходим по номым ивентам из vk и проверяем их по существующим лаберам 
грубо говоря прослушка и проверка сообщений для дальнейшей обработки
    """
    bot.labeler.load(custom_labeler)

bot.labeler.message_view.register_middleware(NoBotMiddleware) # сложная хуйня
bot.labeler.message_view.register_middleware(RegistrationMiddleware) # на самом деле мне просто лень рассписывать

session_manager = True
ignore_error = True  # Честно говоря не помню для чего эти переменные (что то от рейда и ошибок вробе как)
ask_each_event = True

if __name__ == "__main__":
    bot.loop_wrapper.on_startup += [init_tortoise()]
    bot.run_forever()
