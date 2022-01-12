import pytest

from client_task import Item, CachedClient


@pytest.fixture()
def item_1():
    return Item(1, 'name')


@pytest.fixture()
def items_list():
    return [Item(i, "name") for i in range(10)]


@pytest.fixture()
def client():
    return CachedClient()


@pytest.fixture()
def client_with_cache_get(client):
    setattr(client, 'cache', {1: Item(1, 'name')})
    return client


@pytest.fixture()
def client_with_cache_list(client):
    setattr(client, 'cache', {i: Item(i, "name") for i in range(10)})
    setattr(client, 'list_count', 1)
    return client
