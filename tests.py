from kv_helpers import KVstore
import pytest
import itertools


@pytest.fixture
def make_data():
    test_keys = [1, "key", "", 2.0]
    test_values = [1, "value", "", 2.0]
    all_combinations = [
        list(zip(each_permutation, test_values))
        for each_permutation in itertools.permutations(test_keys, len(test_values))
    ]
    return all_combinations


def test_get(make_data):
    for pair in make_data:
        kv = KVstore()
        kv.put(pair[0], pair[1])
        assert kv.get(pair[0]) == pair[1]


def test_get_negative():
    kv = KVstore()
    kv.put(1, 3)
    assert kv.get(2) == "No such key"


def test_delete(make_data):
    for pair in make_data:
        kv = KVstore()
        kv.put(pair[0], pair[1])
        kv.delete(pair[0])
        assert kv.get(pair[0]) == "No such key"
