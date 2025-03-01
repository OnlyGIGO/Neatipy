
from datastructures import DoublyLinkedList
from datastructures import Node
from dataclasses import is_dataclass

class LRUCache():
    cache = {}
    doubly_linked_list = DoublyLinkedList()
    _immutables = (tuple, str, int, float, bool, frozenset)

    @staticmethod
    def lru_cache(max_size=128):
        """LRU cache decorator."""
        def decorator(func):
            def wrapper(*args, **kwargs):
                obj = args[0]
                if isinstance(obj, LRUCache._immutables) or ((is_dataclass(obj) and getattr(obj, '__dataclass_fields__', None) and hasattr(obj, '__hash__'))):
                    node = LRUCache.cache.get(obj, None)
                    if node is None:
                        ret_val = func(*args, **kwargs)
                        new_node = Node(ret_val, obj)
                        LRUCache.cache[obj] = new_node
                        LRUCache.doubly_linked_list.insert_to_head(new_node)
                        if LRUCache.doubly_linked_list.size > max_size:
                            key = LRUCache.doubly_linked_list.tail.key
                            LRUCache.doubly_linked_list.remove_from_tail()
                            LRUCache.cache.pop(key)
                        return ret_val
                    else:
                        LRUCache.doubly_linked_list.remove(node)
                        LRUCache.doubly_linked_list.insert_to_head(node)
                        return node.val
                else:
                    return func(*args, **kwargs)
            return wrapper
        return decorator
