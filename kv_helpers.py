from threading import Lock


class KVstore:
    def __init__(self) -> None:
        self.in_memory_storage = {}
        self.lock = Lock()

    def put(self, k, val):
        with self.lock:
            self.in_memory_storage[k] = val

    def get(self, k):
        try:
            return self.in_memory_storage[k]
        except KeyError:
            return "No such key"

    def delete(self, k):
        with self.lock:
            self.in_memory_storage.pop(k)
