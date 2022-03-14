from dev_up import DevUpAPI
from vkbottle.bot import BotLabeler
from vkbottle.bot import Message

from config import dev_up_key
from utils import get_forward, join, resolve_url

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="стикеры")
async def greetin(message: Message):
    """
    ууууф ну давайте разберем
    Используем опять dev_up
    отправляем запрос на https://api.dev-up.ru/method/vk.getStickers
    в формате json
    {
        "key": "string",
        "user_id": 0
    }
    получаем вот такой ответ:
    {
        "response": {
        "user_id": 0,
        "count": 0,
        "stickers": [],
        "price": {}
        }
    }
    удобненько расшифровываем это используя for циклы и библиотеку от dev_up
    """
    if message.reply_message == None:
        vk_user = message.from_id
    else:
        vk_user = message.reply_message.from_id
    us = await message.get_user(user_ids=vk_user)
    try:
        api = DevUpAPI(dev_up_key)
        stickers = api.vk.get_stickers(vk_user).response
        text = f"📄 Пользователь [id{us.id}|{us.first_name} {us.last_name}] " \
               f"имеет {stickers.count} стикеров из {stickers.count_all}\n" \
               f"💰 Стоимость в голосах: {stickers.price.votes}\n" \
               f"💵 Стоимость в рублях: {stickers.price.rub}₽\n\n"
        text_stickers = []
        for sticker in stickers.stickers:
            text_stickers += [f"{sticker.name}"]

        ss = text + join(text_stickers, ", ")
        await message.answer(ss, disable_mentions=1, forward=get_forward(message))

    except Exception as ex:
        await message.answer(message=str(ex))

@bl.message(text="стикеры [id<vk_user:int>|<other>")
async def greetin(message: Message, vk_user: int, **kwargs):
    us = await message.get_user(user_ids=vk_user)
    try:
        api = DevUpAPI(dev_up_key)
        stickers = api.vk.get_stickers(vk_user).response
        text = f"📄 Пользователь [id{us.id}|{us.first_name} {us.last_name}] " \
               f"имеет {stickers.count} стикеров из {stickers.count_all}\n" \
               f"💰 Стоимость в голосах: {stickers.price.votes}\n" \
               f"💵 Стоимость в рублях: {stickers.price.rub}₽\n\n"
        text_stickers = []
        for sticker in stickers.stickers:
            text_stickers += [f"{sticker.name}"]

        ss = text + join(text_stickers, ", ")
        await message.answer(ss)

    except Exception as ex:
        await message.answer(message=str(ex))


@bl.message(text="стикеры <vk_user>")
async def greetin(message: Message, vk_user: str):
    """все тоже саоме кроме получения ссылки
    мы получаем ее через утилиту resolve_url"""
    id_user = await resolve_url(message, vk_user)
    us = await message.get_user(user_ids=id_user)
    try:
        api = DevUpAPI(dev_up_key)
        stickers = api.vk.get_stickers(id_user).response
        text = f"📄 Пользователь [id{us.id}|{us.first_name} {us.last_name}] " \
               f"имеет {stickers.count} стикеров из {stickers.count_all}\n" \
               f"💰 Стоимость в голосах: {stickers.price.votes}\n" \
               f"💵 Стоимость в рублях: {stickers.price.rub}₽\n\n"
        text_stickers = []
        for sticker in stickers.stickers:
            text_stickers += [f"{sticker.name}"]

        ss = text + join(text_stickers, ", ")
        await message.answer(ss, disable_mentions=1, forward=get_forward(message))

    except Exception as ex:
        await message.answer(message=str(ex))


@bl.message(text="подписки")
async def kik_bot(message: Message):
    "бля ну точно такая же механика что и выше"
    if message.reply_message == None:
        vk_user_id = message.from_id
    else:
        vk_user_id = message.reply_message.from_id
    us = await message.get_user(user_ids=vk_user_id)

    api = DevUpAPI(dev_up_key)

    custom = api.make_request(
        "vk.userGetSubscriptions",
        data=dict(user_id=f"{vk_user_id}"),
        dataclass=dict
    )
    print(custom)
    if custom['response']['count'] == 0:
        return f"Пользователь [id{us.id}|{us.first_name} {us.last_name}] ни на кого не подписан"
    else:
        i = 0
        text = f"Пользователь [id{us.id}|{us.first_name} {us.last_name}] подписан на {custom['response']['count']} человек\n\n"
        while custom['response']['count'] > i:
            sss = custom["response"]["subscriptions"][i]
            uss = await message.get_user(user_ids=sss)
            text += f'[id{uss.id}|{uss.first_name} {uss.last_name}]\n'
            i += 1
    await message.answer(text, disable_mentions=1, forward=get_forward(message))


@bl.message(text="подписки <vk_user_id>")
async def kik_bot(message: Message, vk_user_id: str):
    "бля ну точно такая же механика что и выше"
    id_user = await resolve_url(message, vk_user_id)
    us = await message.get_user(user_ids=id_user)

    api = DevUpAPI(dev_up_key)

    custom = api.make_request(
        "vk.userGetSubscriptions",
        data=dict(user_id=f"{vk_user_id}"),
        dataclass=dict
    )
    print(custom)
    if custom['response']['count'] == 0:
        return f"Пользователь [id{us.id}|{us.first_name} {us.last_name}] ни на кого не подписан"
    else:
        i = 0
        text = f"Пользователь [id{us.id}|{us.first_name} {us.last_name}] подписан на {custom['response']['count']} человек\n\n"
        while custom['response']['count'] > i:
            sss = custom["response"]["subscriptions"][i]
            uss = await message.get_user(user_ids=sss)
            text += f'[id{uss.id}|{uss.first_name} {uss.last_name}]\n'
            i += 1
    await message.answer(text, disable_mentions=1, forward=get_forward(message))
