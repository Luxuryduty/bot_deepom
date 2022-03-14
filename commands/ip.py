from dev_up import DevUpAPI
from vkbottle.bot import BotLabeler

from config import dev_up_key
from utils import *

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="ip <lll>")
async def greetin(message: Message, lll: str):
    """
    Запрос на https://api.dev-up.ru/method/utils.getWebInfo
    в таком виде
    {
        "key": "string",
        "address": "string"
    }
    Далее ответ и расшифровка конфига
    {
        "response": {
        "ip_info": {},
        "ip_geo": {}
        }
    }
    """
    api = DevUpAPI(dev_up_key)
    web_info = api.utils.get_web_info(lll).response

    text = (
        f"Информация об веб-адресе <<{lll}>>\n"
        f"Адрес: {get_or_none(web_info.ip_info.address)}\n"
        f"IP: {get_or_none(web_info.ip_info.ip)}\n"
        f"DNS: {get_or_none(web_info.ip_info.dns)}\n"
        f"Offset: {get_or_none(web_info.ip_info.offset)}\n"
    )
    if web_info.ip_info.organization:
        org = web_info.ip_info.organization
        text += f"Организация: {get_or_none(org.name)} | AS: {get_or_none(org.as_code)} {get_or_none(org.as_name)}\n"
        del org
    if web_info.ip_info.connection:
        conn = web_info.ip_info.connection
        text += (
            f"\nСоединение:\n"
            f"Статус: {get_or_none(conn.status)}\n"
            f"Прокси: {b2s(conn.proxy)}\n"
            f"web-server: {b2s(conn.web_server)}\n"
            f"Прямое соединение: {b2s(conn.direct_connection)}\n"
            f"Мобильная сеть: {b2s(conn.mobile_network)}\n"
        )
        del conn

    text += (
        f"\nГород: {get_or_none(web_info.ip_geo.city)} {get_or_none(web_info.ip_geo.zip)}\n"
        f"Валюта: {get_or_none(web_info.ip_geo.currency)}\n"
        f"Часовой пояс: {get_or_none(web_info.ip_geo.timezone)}\n\n"
    )

    if web_info.ip_geo.continent:
        info = web_info.ip_geo.continent
        text += f"Континент: {get_or_none(info.code)} {get_or_none(info.name)}\n"
        del info
    if web_info.ip_geo.country:
        info = web_info.ip_geo.country
        text += f"Страна: {get_or_none(info.code)} {get_or_none(info.name)}\n"
        del info
    if web_info.ip_geo.region:
        info = web_info.ip_geo.region
        text += f"Регион/город: {get_or_none(info.code)} {get_or_none(info.name)}\n"
        del info
    await message.answer(message=text,
                         **dict(
                             lat=web_info.ip_geo.coordinates.latitude,
                             long=web_info.ip_geo.coordinates.longitude,
                         ) if web_info.ip_geo.coordinates else dict(), disable_mentions=1,
                         forward=get_forward(message))
