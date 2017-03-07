from mappers.item import ItemMapper
from models import Item
from services.repositories.base import BaseRepository


class ItemRepository(BaseRepository):

    Table = Item.__table__
    Mapper = ItemMapper
