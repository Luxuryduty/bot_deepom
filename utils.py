"""а здесь мы буем хранить функции которые мы будем вызывать в других файлах
по сути сюда можно запихнуть проверку на админа и другие функции но я вспомнил об этом только когда писал
документацию по этому формат сообщения останется рядом с ключиками
Вообще сюда можно было бы вставить еще проверку на админа и тому подобное но мне лень переписывать код по этому не будем"""
import json
import re
import vk_api
import config
from typing import TypeVar, Union, Iterable

from vkbottle.bot import Message

# Да я передумал и решил сделать красиво...
T = TypeVar("T")


def get_forward(m: Message) -> dict:
    "ВИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИ ГООООООООООООООВНОООООООКОООООООООООООООООД"
    return json.dumps(dict(
        peer_id=m.peer_id,
        conversation_message_ids=m.conversation_message_id,
        is_reply=True
    ), ensure_ascii=False)


def join(data: Union[str, Iterable], separator: str = ",") -> str:
    "Удобная работа со списком которая формирует сообщения заботливо решая нужна ли там запятая или нет"
    if isinstance(data, str):
        data = [data]
    if not data:
        return ''
    return separator.join([str(obj) for obj in data])


async def resolve_url(e: Message, url):
    "Функция для получения user_id"\
    "Да я знаю что это говнокод но мне не заплатили за качественное определение ссылок:)"
    screen_name = url.split('/')[-1]
    id_ = await e.ctx_api.utils.resolve_screen_name(screen_name)
    print(id_.object_id)
    if id_.object_id:
        return id_.object_id
    else:
        url1 = re.sub('[@*]', '', url)
        print(url1)
        us_id = re.sub('\D', '', url1)
        print(us_id)
        return us_id


def get_or_none(value: T) -> Union[T, str]:
    if value is None:
        return "N/A"
    return value


def b2s(value: bool) -> str:
    if value is None:
        return "N/A"
    return "✅" if value else "🚫"


def get_user_id_by_domain(user_domain: str):
    """Поиск ID по домену"""
    vk = vk_api.VkApi(token=config.main_token)

    obj = vk.method('utils.resolveScreenName', {"screen_name": user_domain})

    if isinstance(obj, list):
        return
    if obj['type'] == 'user':
        return obj["object_id"]

def search_user_ids(text):
    result = []

    regex = r"(?:vk\.com\/(?P<user>[\w\.]+))|(?:\[id(?P<user_id>[\d]+)\|)"


    for user_domain, user_id in re.findall(regex, text):
        if user_domain:
            result.append(get_user_id_by_domain(user_domain))
        if user_id:
            result.append(int(user_id))

    _result = []
    for r in result:
        if r is not None:
            _result.append(r)
    return _result


