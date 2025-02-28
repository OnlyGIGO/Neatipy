from weakref import WeakKeyDictionary
from doubly_linked_list import DoublyLinkedList
from node import Node
class LRUCache():
    static_object_dict={}
    dynamic_object_dict=WeakKeyDictionary()
    doubly_linked_list=DoublyLinkedList()
    _immutables=(tuple,str,int,float,)

    @staticmethod
    def _remove_from_dict(key:any)->None:
        """Removes from either static or dynamic library depending on the key type"""
        if isinstance(key,LRUCache._immutables):
            LRUCache.static_object_dict.pop(key)
        else:
            LRUCache.dynamic_object_dict.pop(key)

    @staticmethod
    def lru_cache(func,max_size=128):
        """LRU cache decorator"""
        def wrapper(*args,**kwargs):
            obj=args[0]
            if isinstance(obj,LRUCache._immutables):
                node=LRUCache.static_object_dict.get(obj,None)
                if node is None:
                    ret_val=func()
                    new_node=Node(ret_val,obj)
                    LRUCache.static_object_dict[obj]=new_node  
                    LRUCache.doubly_linked_list.insert_to_head(new_node)
                    if LRUCache.doubly_linked_list.size>max_size:
                        key=LRUCache.doubly_linked_list.tail.key
                        LRUCache.doubly_linked_list.remove_from_tail()
                        LRUCache._remove_from_dict(key)
                    return ret_val
                else:
                    LRUCache.doubly_linked_list.remove(node)
                    LRUCache.doubly_linked_list.insert_to_head(node)
                    return node.val
            else:
                node=LRUCache.dynamic_object_dict.get(obj,None)
                if node is None:
                    ret_val=func()
                    new_node=Node(ret_val,obj)
                    LRUCache.dynamic_object_dict[obj]=new_node  
                    LRUCache.doubly_linked_list.insert_to_head(new_node)
                    if LRUCache.doubly_linked_list.size>max_size:
                        key=LRUCache.doubly_linked_list.tail.key
                        LRUCache.doubly_linked_list.remove_from_tail()
                        LRUCache._remove_from_dict(key)
                    return ret_val
                else:
                    LRUCache.doubly_linked_list.remove(node)
                    LRUCache.doubly_linked_list.insert_to_head(node)
                    return node.val
        return wrapper