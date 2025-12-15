class HashMap:
    def __init__(self, initial_capacity=8, load_factor=0.75):
        if initial_capacity <= 0:
            raise ValueError("initial_capacity must be a positive integer")
        if load_factor <= 0 or load_factor >= 1:
            raise ValueError("load_factor must be between 0 and 1 (exclusive)")

        # capacity should be at least 1
        self._capacity = initial_capacity
        self._load_factor = load_factor
        self._size = 0

        # buckets: list of chains; each chain is a list of (key, value)
        self._buckets = [[] for _ in range(self._capacity)]

    # ---------- Public API ----------

    def put(self, key, value):
        """Insert or update a key-value pair."""
        if self._needs_resize(next_size=self._size + 1):
            self._resize(self._capacity * 2)

        bucket = self._bucket_for_key(key)

        # Update existing key if present
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Otherwise insert new
        bucket.append((key, value))
        self._size += 1

    def get(self, key, default=None):
        """Return value for key or default if key not found."""
        bucket = self._bucket_for_key(key)
        for k, v in bucket:
            if k == key:
                return v
        return default

    def remove(self, key):
        """Remove key and return its value. Raise KeyError if not found."""
        bucket = self._bucket_for_key(key)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # remove pair
                bucket.pop(i)
                self._size -= 1
                return v
        raise KeyError(key)

    def contains(self, key):
        """Return True if key exists."""
        bucket = self._bucket_for_key(key)
        for k, _ in bucket:
            if k == key:
                return True
        return False

    def size(self):
        """Return number of stored key-value pairs."""
        return self._size

    def clear(self):
        """Remove all entries."""
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

    def keys(self):
        """Yield keys."""
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k

    def values(self):
        """Yield values."""
        for bucket in self._buckets:
            for _, v in bucket:
                yield v

    def items(self):
        """Yield (key, value) pairs."""
        for bucket in self._buckets:
            for k, v in bucket:
                yield (k, v)

    # ---------- Pythonic dunder methods ----------

    def __getitem__(self, key):
        sentinel = object()
        value = self.get(key, sentinel)
        if value is sentinel:
            raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, key):
        return self.contains(key)

    def __len__(self):
        return self._size

    def __iter__(self):
        """Iterate over keys by default, like dict."""
        return self.keys()

    def __repr__(self):
        pairs = ", ".join([f"{k!r}: {v!r}" for k, v in self.items()])
        return f"HashMap({{{pairs}}})"

    # ---------- Internals ----------

    def _bucket_index(self, key):
        # Python's hash can be negative; modulo handles it fine.
        return hash(key) % self._capacity

    def _bucket_for_key(self, key):
        return self._buckets[self._bucket_index(key)]

    def _needs_resize(self, next_size):
        return (next_size / self._capacity) > self._load_factor

    def _resize(self, new_capacity):
        old_items = list(self.items())

        self._capacity = new_capacity
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        for k, v in old_items:
            # Reinsert into new buckets (rehash)
            bucket = self._bucket_for_key(k)
            bucket.append((k, v))
            self._size += 1
