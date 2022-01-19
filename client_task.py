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
            print(f'Get {item_id} from cache')
            return self.cache[item_id]

        time.sleep(1)
        g_object = self.client.get_object(item_id)
        # add an item to the cache
        self.cache[item_id] = g_object
        return g_object

    def list_objects(self) -> List[Item]:
        if self.list_count > 0:
            print('Get list from cache')
            return [v for k, v in self.cache.items()]

        time.sleep(1)
        result_list = self.client.list_objects()
        # add items to the cache
        for item in result_list:
            self.cache.update({item.id: item})
        self.list_count += 1
        return result_list

    def put_object(self, item: Item) -> None:
        item_id = item.id
        if item_id in self.cache:
            print('Put in cache')
            self.cache[item_id] = item

        time.sleep(1)


def main():
    some_client = SomeClient()
    Cclient = CachedClient(some_client)
    print(Cclient.get_object(2))
    print(Cclient.get_object(2))
    print(Cclient.cache)
    print(Cclient.list_objects())
    print(Cclient.cache)
    print(Cclient.list_objects())
    Cclient.put_object(Item(id=2, name='name_2!!'))
    print(Cclient.cache)


if __name__ == '__main__':
    main()
