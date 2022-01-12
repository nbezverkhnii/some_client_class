import time
from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    id: int
    name: str


class SomeClient:
    def get_object(self, item_id) -> Item:
        time.sleep(1)
        return Item(item_id, "name")

    def list_objects(self) -> List[Item]:
        time.sleep(1)
        return [Item(i, "name") for i in range(10)]

    def put_object(self, item: Item) -> None:
        time.sleep(1)


class CachedClient:
    def __init__(self):
        self.cache = dict()
        self.list_count = 0

    def get_object(self, item_id: int) -> Item:
        if item_id in self.cache:
            print(f'Get {item_id} from cache')
            return self.cache[item_id]

        time.sleep(1)
        self.cache[item_id] = Item(item_id, "name")
        return Item(item_id, "name")

    def list_objects(self) -> List[Item]:
        if self.list_count > 0:
            print('Get list from cache')
            return [v for k, v in self.cache.items()]

        time.sleep(1)
        self.cache.update({i: Item(i, "name") for i in range(10)})
        self.list_count += 1
        return [Item(i, "name") for i in range(10)]

    def put_object(self, item: Item) -> None:
        item_id = item.id
        if item_id in self.cache:
            print('Put in cache')
            self.cache[item_id] = item

        time.sleep(1)


def main():
    Cclient = CachedClient()
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
