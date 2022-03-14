from dev_up import DevUpAPI
from vkbottle.bot import BotLabeler
from vkbottle.bot import Message

from config import dev_up_key
from utils import get_forward, resolve_url

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="группы")
async def greetin(message: Message):
    """
    блин ну теперь группы
    отправляем запрос на
    https://api.dev-up.ru/method/vk.getGroups
    в json формате
    {
        "key": "string",
        "user_id": 0
    }
    получаем вот такой ответ:
    {
        "response": {
            "user_id": 0,
            "count": 0,
            "groups": [],
            "description": {}
            }
    }
    удобненько расшифровываем это используя for циклы и библиотеку от dev_up
    """
    if message.reply_message == None:
        vk_user = message.from_id
    else:
        vk_user = message.reply_message.from_id
    us = await message.get_user(user_ids=vk_user)
    dev_api = DevUpAPI(dev_up_key)
    user_groups = dev_api.vk.get_groups(vk_user)
    text = (
        f"📄 Пользователь [id{us.id}|{us.first_name} {us.last_name}] "
        f"имеет {user_groups.response.count} групп\n\n"
    )
    for group in user_groups.response.groups:
        text += f"[club{group.id}|{group.name}] -> {group.members_count} участников\n"
    await message.answer(text, disable_mentions=1, forward=get_forward(message))

@bl.message(text="группы [id<vk_user:int>|<other>")
async def greetin(message: Message, vk_user: int, **kwargs):
    us = await message.get_user(user_ids=vk_user)
    dev_api = DevUpAPI(dev_up_key)
    user_groups = dev_api.vk.get_groups(vk_user)
    text = (
        f"📄 Пользователь [id{us.id}|{us.first_name} {us.last_name}] "
        f"имеет {user_groups.response.count} групп\n\n"
    )
    for group in user_groups.response.groups:
        text += f"[club{group.id}|{group.name}] -> {group.members_count} участников\n"
    return text


@bl.message(text="группы <vk_user>")
async def greetin(message: Message, vk_user: int):
    id_ = await resolve_url(message, vk_user)
    us = await message.get_user(user_ids=id_)
    dev_api = DevUpAPI(dev_up_key)
    user_groups = dev_api.vk.get_groups(id_)
    text = (
        f"📄 Пользователь [id{us.id}|{us.first_name} {us.last_name}] "
        f"имеет {user_groups.response.count} групп\n\n"
    )
    for group in user_groups.response.groups:
        text += f"[club{group.id}|{group.name}] -> {group.members_count} участников\n"
    await message.answer(text, disable_mentions=1, forward=get_forward(message))
