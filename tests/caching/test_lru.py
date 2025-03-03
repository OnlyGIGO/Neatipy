from neatipy import LRUCache


def test_lru_with_immutable():
    immutable = (
        1,
        2,
        3,
    )

    @LRUCache.lru_cache(max_size=128)
    def func(immutable):
        return str(id(immutable))

    func(immutable)
    assert func._cache.get(id(immutable)).val == str(
        id(immutable)
    )  # same as func's return value meaning it was cached


def test_lru_with_mutable():
    mutable = [1, 2, 3]

    @LRUCache.lru_cache(max_size=128)
    def func(mutable):
        return str(id(mutable))

    func(mutable)
    assert func._cache.get(id(mutable), 0) == 0
