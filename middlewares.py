from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from models import User


class NoBotMiddleware(BaseMiddleware[Message]):
    "Игнорирование ботов по причине нам нужны кожанные мешки:)"

    async def pre(self):
        return self.event.from_id > 0


class RegistrationMiddleware(BaseMiddleware[Message]):

    async def pre(self):
        db_user = await User.get_or_new(id=self.event.from_id)

        return db_user.rank >= 0
