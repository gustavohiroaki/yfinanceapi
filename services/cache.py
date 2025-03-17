import os
import ast

class Cache:
    def __init__(self, r):
        self.r = r
        self.cache_expiration = 60 * 60 * int(os.environ.get("CACHE_EXPIRATION_HOURS", 4))

    def set(self, key, value):
        self.r.set(key, str(value), ex=self.cache_expiration)

    def get(self, key):
        result_in_bytes = self.r.get(key)
        if result_in_bytes:
            return ast.literal_eval(result_in_bytes.decode())
        return None
