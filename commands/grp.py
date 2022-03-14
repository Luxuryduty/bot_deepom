import json

from vkbottle.bot import BotLabeler, Message

import config
from utils import get_forward

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text=["2ис1", "вк 2ис1"])
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Группа: {faile["grp_1"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["обновить 2ис1 <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['grp_1'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["2пи1", "вк 2пи1"])
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Группа: {faile["grp_2"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["обновить 2пи1 <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['grp_2'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["3п1", "вк 3п1"])
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Группа: {faile["grp_3"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["обновить 3п1 <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['grp_3'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо


@bl.message(text=["3пи1", "вк 3пи1"])
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Группа: {faile["grp_4"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["обновить 3пи1 <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['grp_4'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["4п1", "вк 4п1"])
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Группа: {faile["grp_5"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["обновить 4п1 <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['grp_5'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["4пи1", "вк 4пи1"])
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Группа: {faile["grp_6"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["обновить 4пи1 <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))  # Определяем какой файл открыть доставая путь до файла из config.py
    if not message.from_id in admin['admins']:  # Проверяем админ ли этот человек
        return
    admin['grp_6'] = url  # Обновляем ссылку

    with open(config.faile, 'w') as f:  # Записываем новый конфиг
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо



