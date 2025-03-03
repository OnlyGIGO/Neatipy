from neatipy.datastructures import DoublyLinkedList
from neatipy.datastructures import Node
from dataclasses import is_dataclass
from typing import Callable


class LRUCache:
    _immutables = (tuple, str, int, float, bool, frozenset)

    @staticmethod
    def is_immutable(obj: any) -> bool:
        """Is immutable helper function"""
        if isinstance(obj, LRUCache._immutables):
            return True
        if (
            is_dataclass(obj)
            and getattr(obj, "__dataclass_fields__", None)
            and hasattr(obj, "__hash__")
        ):
            return all(
                LRUCache.is_immutable(getattr(obj, field))
                for field in obj.__dataclass_fields__
            )
        return False

    @staticmethod
    def lru_cache(max_size: int = 128) -> Callable:
        """LRU cache decorator."""

        def decorator(func):
            cache = {}
            doubly_linked_list = DoublyLinkedList()

            def wrapper(*args, **kwargs):
                if not args:
                    return func(*args, **kwargs)
                obj = args[0]
                if isinstance(obj, LRUCache._immutables) or (
                    is_dataclass(obj)
                    and getattr(obj, "__dataclass_fields__", None)
                    and hasattr(obj, "__hash__")
                    and all(
                        LRUCache.is_immutable(getattr(obj, field))
                        for field in obj.__dataclass_fields__
                    )
                ):
                    node = cache.get(id(obj), None)
                    if node is None:
                        ret_val = func(*args, **kwargs)
                        new_node = Node(ret_val, id(obj))
                        cache[id(obj)] = new_node
                        doubly_linked_list.insert_to_head(new_node)
                        if doubly_linked_list.size > max_size:
                            key = doubly_linked_list.tail.key
                            doubly_linked_list.remove_from_tail()
                            cache.pop(key)
                        return ret_val
                    else:
                        doubly_linked_list.remove(node)
                        doubly_linked_list.insert_to_head(node)
                        return node.val
                else:
                    return func(*args, **kwargs)

            return wrapper

        return decorator
