def test_get_object_from_cache(capsys, cached_client_get, item_1):
    assert cached_client_get.get_object(1) == item_1

    captured = capsys.readouterr()
    assert captured.out == f'Get {item_1.id} from cache\n'


def test_update_cache_after_get(cached_client_get, new_item):
    id = new_item.id
    cached_client_get.get_object(id)
    assert id in cached_client_get.cache


def test_list_from_cache(capsys, cached_client_list, items_list):
    assert cached_client_list.list_objects() == items_list

    captured = capsys.readouterr()
    assert captured.out == 'Get list from cache\n'


def test_update_cache_after_list(cached_client, items_list):
    cached_client.list_objects()
    cached_client.cache == items_list


def test_update_cache_after_put(capsys, cached_client_list, changed_item):
    cached_client_list.put_object(changed_item)
    assert cached_client_list.cache[changed_item.id] == changed_item

    captured = capsys.readouterr()
    assert captured.out == 'Put in cache\n'
