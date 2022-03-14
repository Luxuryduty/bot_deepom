from tortoise import Model, fields


class User(Model):
    """
    Модель базы данных юзеров
    Важная вещь для работы бота и преподов
    основной параметр vk_id
    id = юзер вк айди (по нему мы определяем кто)
    rank = ранг юзера (-1 игнор, 0, гость (студент) 1 (препод) а выше нету потому что нету норм системы админов так что пофик
    time_work = Время работы препода
    tel = Телефон препода (Чисто по приколу созраним строку)
    mail = почта
    predmet = предмет который ведет препод
    kab = Кабинет препода (должно быть интовое значение но кабинетов может быть несколько так что похуй)
    opis = Описание (немного о себе хз зачем нужно просто хочу)
    """
    id = fields.IntField(pk=True)  # вк айди
    rank = fields.IntField(default=0)
    time_work = fields.CharField(max_length=256, null=True)
    tel = fields.CharField(max_length=256, null=True)
    mail = fields.CharField(max_length=256, null=True)
    predmet = fields.CharField(max_length=256, null=True)
    kab = fields.CharField(max_length=256, null=True)
    opis = fields.CharField(max_length=256, null=True)


    @classmethod
    async def get_or_new(cls, **kwargs) -> "User":
        user, _ = await cls.get_or_create(**kwargs)
        return user