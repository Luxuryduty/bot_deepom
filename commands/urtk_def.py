import json

from dev_up import DevUpAPI
from vkbottle.bot import BotLabeler, Message

import config
from utils import get_forward

bl = BotLabeler()
bl.vbml_ignore_case = True

"""
Этот файл нужен для работы с расписанием
да у меня не получилось написать норм парс сайта по этому будем использовать команду обнови и админов 
в будующем мб обновлю

UPD: вот и время тебя обновить кусок ты говнокода
"""


@bl.message(text=["обнови <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['url'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["обновить телефон <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['telefon'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["обновить факс <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['faks'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["обновить почту <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['mail'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["обновить сайт <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['sait'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["обновить адрес <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['strid'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["помощь"])
async def greetng(message: Message, ):
    admin = json.load(open(config.faile))  # Определяем файл который читаем
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        handle = open("commands_user.txt", "r", encoding="utf-8")
        data = handle.read()
        return str(data)
    else:
        handle = open("commands.txt", "r", encoding="utf-8")
        data = handle.read()
        return str(data)


@bl.message(text=["контакты", 'адрес', "связь"])
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Телефон: {faile["telefon"]}\n' \
           f'Факс: {faile["faks"]}\n' \
           f'Почта: {faile["mail"]}\n' \
           f'Адрес: {faile["strid"]}\n' \
           f'Сайт: {faile["sait"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text="сайт")
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Сайт: {faile["sait"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

# я не хочу об этом говорить...
@bl.message(text="расписание")
async def greeting(message: Message):
    faile = json.load(open(config.faile))  # определяем файл
    url = faile['url']  # определяем ссылку
    api = DevUpAPI(config.dev_up_key)  # небольшая авторизация через dev_up
    # Почему dev_up? хз у них созд прикольный я дружу с ним

    custom = api.make_request(
        "utils.createShortLink",
        data=dict(url=url),
        dataclass=dict
    )
    """
Ооох разбираем custom
мы отправляем запрос на https://api.dev-up.ru/method/utils.createShortLink
код запроса в json выглядит вот так:
{
  "key": "string",
  "url": "string"
}
Ответ в json выгляит так:
{
  "response": {
    "id": 0,
    "create_vk": 0,
    "original_url": "string",
    "create_date": 0,
    "notifications": true,
    "link": {
      "url": "string",
      "code": "string"
    }
  }
}

    """
    url_dev = custom['response']['link']['url']  # Из ответа мы достаем url а остальное нам не нужно если мы не ведем статистику

    await message.answer(attachment=url_dev, disable_mentions=1, forward=get_forward(message))




@bl.message(text=["звонки"])
async def greeting(message: Message):
    # Просто отпровлаем фото в attachment
    # Да мне было лень делать attachment на выгрузку из корня
    await message.answer(attachment="photo-207904771_457239017?api_access_key=fa18d546bf9e1a00aa", disable_mentions=1,
                         forward=get_forward(message))


@bl.message(text=["кто админ"])
async def greeting(message: Message):
    ranks_4 = 'Администраторы нашего бота:\n\n'  # изначальная фраза которая есть везде
    admin = json.load(open(config.faile))  # Определяем файл откуда возьмем список админов
    for user in await message.ctx_api.users.get(user_ids=admin['admins']):
        """ 
        Испольхуя vk_api мы получаем профили но нам нужны только их id и имена
        в запроссе мы отправляем список id из файла с админаи и сразу получаем список с json их профилей 
        выглядит ответ примерно так:
        {
            "response": [{
                "id": 210700286,
                "first_name": "Lindsey",
                "last_name": "Stirling",
                "is_closed": false,
                "can_access_closed": true,
                "photo_50": "https://sun9-39.u...gaEKflurs&ava=1",
                "verified": 1
            }]
        }
        Но сипользуя магию vkbottle мы достаем из них id имя и фамилию
        """
        ranks_4 += f"[id{user.id}|{user.first_name} {user.last_name}]\n"  # и добовляем это в сообщение
    await message.answer(message=ranks_4, disable_mentions=1, forward=get_forward(message))
