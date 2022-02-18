import time
from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    id: int
    name: str


class SomeClient:
    def get_object(self, item_id: int) -> Item:
        time.sleep(1)
        return Item(item_id, "name")

    def list_objects(self) -> List[Item]:
        time.sleep(1)
        return [Item(i, "name") for i in range(10)]

    def put_object(self, item: Item) -> None:
        time.sleep(1)


class CachedClient:
    def __init__(self, client: SomeClient):
        self.client = client
        self.cache = dict()
        self.list_count = 0

    def get_object(self, item_id: int) -> Item:
        if item_id in self.cache:
            return self.cache[item_id]

        g_object = self.client.get_object(item_id)
        # add an item to the cache
        self.cache[item_id] = g_object
        return g_object

    def list_objects(self) -> List[Item]:
        if self.list_count > 0:
            return [v for k, v in self.cache.items()]

        result_list = self.client.list_objects()
        # add items to the cache
        for item in result_list:
            self.cache.update({item.id: item})
        self.list_count += 1
        return result_list

    def put_object(self, item: Item) -> None:
        item_id = item.id
        if item_id in self.cache:
            self.cache[item_id] = item

        self.client.put_object(item)


def dry_run() -> None:
    some_client = SomeClient()
    client = CachedClient(some_client)
    print(client.get_object(2))
    print(client.get_object(2))
    print(client.cache)
    print(client.list_objects())
    print(client.cache)
    print(client.list_objects())
    client.put_object(Item(id=2, name='name_2!!'))
    print(client.cache)


if __name__ == '__main__':
    dry_run()
