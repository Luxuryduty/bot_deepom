import time
from pyqiwip2p import QiwiP2P
from vkbottle.bot import BotLabeler
from vkbottle.bot import Message
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from utils import get_forward
from config import main_token, QIWI_PRIV_KEY

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text=["пинг"])
async def greeting(message: Message):
    await message.answer(f"Pong\nОтвет доставлен за {round(time.time() - message.date, 2)} секунд", disable_mentions=1,
                         forward=get_forward(message))



@bl.message(text=["ссыль"])
async def greeting(message: Message):
    "дает ссылку на беседу (хз зачем)"
    vk = vk_api.VkApi(token=main_token)
    link_chat = vk.method('messages.getInviteLink', {'peer_id': message.peer_id, 'reset': '0'})
    return str(link_chat)





@bl.message(text=["донат <url:int>", "купить <url:int>"])
async def greeting(message: Message, url: int):
    "Да я тоже хочу кушать"
    vk = vk_api.VkApi(token=main_token)
    p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY, default_amount=148)
    new_bill = p2p.bill(amount=url, lifetime=120)
    s = (new_bill.pay_url)
    q = vk.method("utils.getShortLink", {"url": s, "private": 0})["short_url"]
    return str(q)
