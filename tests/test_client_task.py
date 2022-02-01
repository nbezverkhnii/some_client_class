def test_cache_logic_get(cached_client_with_get_cache):
    cached_client_with_get_cache.get_object(1)
    cached_client_with_get_cache.client.get_object.assert_not_called()


def test_cache_logic_list(cached_client_with_list_cache):
    cached_client_with_list_cache.list_objects()
    cached_client_with_list_cache.client.list_objects.assert_not_called()


def test_cache_logic_put_with_empty_cache(cached_client, item_1):
    cached_client.put_object(item_1)
    cached_client.client.put_object.assert_called()


def test_cache_logic_put_with_cache(cached_client_with_list_cache, item_1):
    cached_client_with_list_cache.put_object(item_1)
    cached_client_with_list_cache.client.put_object.assert_called()


def test_get_object_from_cache(cached_client_with_get_cache, item_1):
    assert cached_client_with_get_cache.get_object(1) == item_1


def test_update_cache_after_get(cached_client_with_get_cache, new_item):
    id = new_item.id
    cached_client_with_get_cache.get_object(id)
    assert id in cached_client_with_get_cache.cache


def test_list_from_cache(cached_client_with_list_cache, items_list):
    assert cached_client_with_list_cache.list_objects() == items_list


def test_update_cache_after_list(cached_client, items_list):
    cached_client.list_objects()
    cached_client.cache == items_list


def test_update_cache_after_put(cached_client_with_list_cache, changed_item):
    cached_client_with_list_cache.put_object(changed_item)
    assert cached_client_with_list_cache.cache[changed_item.id] == changed_item
