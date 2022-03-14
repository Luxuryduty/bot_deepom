from dev_up import DevUpAPI
from vkbottle.bot import BotLabeler
from vkbottle.bot import Message

from config import dev_up_key
from utils import get_forward

bl = BotLabeler()
bl.vbml_ignore_case = True




@bl.message(text=["плейлисты <music>", "плейлист <music>"])
async def greeting(message: Message, music: str):
    api = DevUpAPI(dev_up_key)

    try:
        custom = api.make_request(
            "vk.searchPlaylists",
            data=dict(q=music),
            dataclass=dict
        )
        print(custom)
        text = f"{custom['response']['msg_response']}"
        await message.answer(message=text, attachment=custom['response']['attachments'], disable_mentions=1,
                             forward=get_forward(message))
    except Exception as ex:
        await message.answer(f'⚠ Ошибка: {ex}', disable_mentions=1, forward=get_forward(message))


@bl.message(text=["песни <music>", "песня <music>", "музыка <music>"])
async def greeting(message: Message, music: str):
    api = DevUpAPI(dev_up_key)

    try:
        custom = api.make_request(
            "vk.searchAudio",
            data=dict(q=music),
            dataclass=dict
        )
        print(custom)
        text = f"{custom['response']['msg_response']}"
        await message.answer(message=text, attachment=custom['response']['attachments'], disable_mentions=1,
                             forward=get_forward(message))
    except Exception as ex:
        await message.answer(f'⚠ Ошибка: {ex}', disable_mentions=1, forward=get_forward(message))
