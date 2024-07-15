# Multi-level Cache System Simulation
# Objective: Design a class `CacheSystem` that simulates a two-level cache (L1 and L2). L1 cache has faster access but lower capacity than L2.
# Parameters:
# - l1_size: Integer representing the number of entries L1 cache can hold.
# - l2_size: Integer representing the number of entries L2 cache can hold.
# Returns:
# - None; methods will handle cache operations.
# Details:
# - Implement methods for `put` (to add or update data) and `get` (to retrieve data).
# - Use an LRU (Least Recently Used) policy for cache eviction when the cache is full.
# - If an item is accessed from L2, it should be moved to L1 (if there's space, otherwise evict the least recently used item from L1).



from collections import OrderedDict

class CacheSystem:
    def __init__(self, l1_size, l2_size):
        self.l1_size = l1_size
        self.l2_size = l2_size
        self.l1_cache = OrderedDict()
        self.l2_cache = OrderedDict()

    def _move_to_l1(self, key, value):
        if key in self.l1_cache:
            self.l1_cache.move_to_end(key)
        else:
            if len(self.l1_cache) >= self.l1_size:
                self.l1_cache.popitem(last=False)
            self.l1_cache[key] = value

    def _move_to_l2(self, key, value):
        if key in self.l2_cache:
            self.l2_cache.move_to_end(key)
        else:
            if len(self.l2_cache) >= self.l2_size:
                self.l2_cache.popitem(last=False)
            self.l2_cache[key] = value

    def put(self, key, value):
        if key in self.l1_cache:
            self.l1_cache[key] = value
            self.l1_cache.move_to_end(key)
        elif key in self.l2_cache:
            self.l2_cache.pop(key)
            self._move_to_l1(key, value)
        else:
            self._move_to_l1(key, value)
            if len(self.l1_cache) > self.l1_size:
                lru_key, lru_value = self.l1_cache.popitem(last=False)
                self._move_to_l2(lru_key, lru_value)

    def get(self, key):
        if key in self.l1_cache:
            self.l1_cache.move_to_end(key)
            return self.l1_cache[key]
        elif key in self.l2_cache:
            value = self.l2_cache.pop(key)
            self._move_to_l1(key, value)
            return value
        return None


cache = CacheSystem(2, 3)
cache.put('a', 1)
cache.put('b', 2)
print(cache.get('a'))  
cache.put('c', 3)
cache.put('d', 4)  
print(cache.get('b'))  
print(cache.get('c'))  

# Example usage:
# cache = CacheSystem(2, 3)
# cache.put('a', 1)
# cache.put('b', 2)
# cache.get('a')  # Expected to access from L1
# cache.put('c', 3)
# cache.put('d', 4)  # Should trigger eviction in L2, moving 'c' to L1, evicting 'b'
# cache.get('b')  # Expected: None
# cache.get('c')  # Expected to move from L1, 'd' remains in L2