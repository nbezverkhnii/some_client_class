def test_cache_logic_get(cached_client):
    cached_client.get_object(1)
    cached_client.client.get_object.assert_called()
    cached_client.client.reset_mock()
    cached_client.get_object(1)
    cached_client.client.get_object.assert_not_called()


def test_cache_logic_list(cached_client):
    cached_client.list_objects()
    cached_client.client.list_objects.assert_called()
    cached_client.client.reset_mock()
    cached_client.list_objects()
    cached_client.client.list_objects.assert_not_called()


def test_cache_logic_put_with_empty_cache(cached_client, item_1):
    cached_client.put_object(item_1)
    cached_client.client.put_object.assert_called()


def test_cache_logic_put_with_cache(cached_client, item_1):
    cached_client.list_objects()
    cached_client.put_object(item_1)
    cached_client.client.put_object.assert_called()


def test_get_object_from_cache(cached_client, item_1):
    cached_client.get_object(1)
    assert cached_client.get_object(1) == item_1


def test_update_cache_after_get(cached_client, new_item):
    object_id = new_item.id
    cached_client.get_object(object_id)
    assert object_id in cached_client.cache


def test_list_from_cache(cached_client, items_list):
    cached_client.list_objects()
    assert cached_client.list_objects() == items_list


def test_update_cache_after_list(cached_client, items_list):
    cached_client.list_objects()
    cached_client.cache == items_list


def test_update_cache_after_put(cached_client, changed_item):
    cached_client.list_objects()
    cached_client.put_object(changed_item)
    assert cached_client.cache[changed_item.id] == changed_item
