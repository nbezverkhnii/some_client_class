import pytest

from client_task import Item, CachedClient


@pytest.fixture()
def item_1():
    return Item(1, 'name')


@pytest.fixture()
def changed_item():
    return Item(1, 'changed_name')


@pytest.fixture()
def new_item():
    return Item(99, 'new_name')


@pytest.fixture()
def items_list():
    return [Item(i, "name") for i in range(10)]


@pytest.fixture
def some_client_mock(item_1, items_list, mocker):
    mock = mocker.Mock()
    mock.get_object.return_value = item_1
    mock.list_objects.return_value = items_list
    mock.put_object.return_value = None
    return mock


@pytest.fixture(name='cached_client')
def cached_client_with_empty_cache(some_client_mock):
    return CachedClient(some_client_mock)


@pytest.fixture()
def cached_client_with_get_cache(cached_client):
    setattr(cached_client, 'cache', {1: Item(1, 'name')})
    return cached_client


@pytest.fixture()
def cached_client_with_list_cache(cached_client):
    setattr(cached_client, 'cache', {i: Item(i, "name") for i in range(10)})
    setattr(cached_client, 'list_count', 1)
    return cached_client
