from bitarray import bitarray
import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        hashes = []
        for i in range(self.num_hashes):
            hash_value = int(hashlib.md5((item + str(i)).encode()).hexdigest(), 16)
            hashes.append(hash_value % self.size)
        return hashes

    def add(self, item):
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))

# Example usage
bf = BloomFilter(size=100, num_hashes=3)
bf.add("test")
print(bf.check("test"))  # True
print(bf.check("not_in_bloom"))  # False
