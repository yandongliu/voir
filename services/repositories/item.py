from models.base import session
from models import Item
from mappers.item import ItemMapper


class ItemRepository(object):

    @classmethod
    def read_one(cls, uuid):
        ItemTable = Item.__table__
        query = ItemTable.select().where(ItemTable.c.uuid == uuid)
        rows = session.execute(query)
        if rows:
            entities = map(ItemMapper.to_entity_from_obj, list(rows))
            return entities[0]

    @classmethod
    def read_all(cls):
        ItemTable = Item.__table__
        query = ItemTable.select()
        rows = session.execute(query)
        if rows:
            entities = map(ItemMapper.to_entity_from_obj, list(rows))
            return entities
