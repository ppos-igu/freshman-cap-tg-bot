from tortoise.models import Model
from tortoise import fields
from settings import ROUTES


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32)
    division = fields.CharField(max_length=32)
    leader = fields.IntField(unique=True)
    progress = fields.IntField(default=0)
    score = fields.IntField(default=0)

    def __str__(self):
        return f'{self.id}: {self.name} [{self.progress}/{len(ROUTES[0])}]'

    async def get_current_station(self):
        station_id = ROUTES[self.id - 1][self.progress]
        return await Station.get(id=station_id)


class Station(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    place = fields.CharField(max_length=64)
    image = fields.CharField(max_length=256, null=True)
    moderator = fields.IntField()
