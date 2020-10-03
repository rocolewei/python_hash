# 用来模拟Hash表
class HashTable:
    def __init__(self):
        # HashTable的大小
        self.size = 11
        # HashTable的 key
        self.slots = [None] * self.size
        # HashTable的 data
        self.data = [None] * self.size

    # Hash函数
    def hashFunction(self, key):
        return key % self.size

    # Hash冲突时的解决函数
    def rehash(self, old_hash):
        return (old_hash+1) % self.size

    # 将键值对放入Hash表
    def put(self, key, data):
        hash_value = self.hashFunction(key)
        # 如果该位置是空
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # 存在相同的key, 覆盖
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            # 该位置被其他的key占用
            else:
                for i in range(self.size):
                    hash_value = self.rehash(hash_value)
                    if self.slots[hash_value] is None or self.slots[hash_value] == key:
                        break
                if self.slots[hash_value] is None:
                    self.slots[hash_value] = key
                    self.data[hash_value] = data
                else:
                    self.data[hash_value] = data

    # 获得该key对应的data
    def get(self, key):
        data = None
        found = False
        position = self.hashFunction(key)
        for i in range(self.size):
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                break
            else:
                if self.slots[position] is None:
                    break
                position = self.rehash(position)
        return data


if __name__ == '__main__':
    h = HashTable()
    h.put(12, '电脑')
    h.put(9, '手机')
    ans = h.get(9)
    print(h.slots)
    print(h.data)
    print(ans)
