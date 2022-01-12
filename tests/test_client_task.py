def test_get_object(client, item_1):
    assert client.get_object(1) == item_1


def test_cache_get_object(capsys, client, client_with_cache_get, item_1):
    assert client.get_object(1) == item_1
    captured = capsys.readouterr()
    assert captured.out == f'Get {item_1.id} from cache\n'


def test_list(client, items_list):
    assert client.list_objects() == items_list


def test_cache_list(capsys, client_with_cache_list, items_list):
    assert client_with_cache_list.list_objects() == items_list
    captured = capsys.readouterr()
    assert captured.out == 'Get list from cache\n'


def test_put_object(client, item_1):
    assert client.put_object(item_1) is None


def test_cache_put_object(capsys, client_with_cache_list, item_1):
    assert client_with_cache_list.put_object(item_1) is None
    captured = capsys.readouterr()
    assert captured.out == 'Put in cache\n'
