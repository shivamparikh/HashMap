# Created by Shivam Parikh
#  Application for KPCB Fellows Program, 2017-2018
#  Fixed Length HashMap Implementation

class Node:

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def iterateAll(self):
        n = self
        while(n):
            yield n
            n = n.next

    def getLast(self):
        n = self
        while(n.next):
            n = n.next
        return n

    def setLast(self, node):
        self.getLast().next=node

    def __str__(self):
        # Recursive string representation of a node/Linked List
        #   Slows runtime
        if self.next:
            temp = "---> %s" % self.next
        else:
            temp = " XX"
        return ("(%s, %s) %s" % (self.key, self.value, temp))

class HashMap:
    # This is the class of the HashMap itself
    #   The offset parameter takes into account a user preference
    #   for a tradeoff on memory or access speed.
    # Offset at 0 yields a bucket size that is the upper nearest
    #   power of 2 from the size specified. At 1, yields a bucket size
    #   that is the lower nearest power of 2.
    # The more buckets, the lower collision probability but the larger the
    #   memory usage for the array storing the information.
    # Default priority is set for access speed because memory is far cheaper
    def __init__(self, size, offset=0):
        self.num_buckets = 1<<(size.bit_length()-offset)
        self.items = 0
        self.max_size = size
        self.array = [None for i in range(self.num_buckets)]
    
    def set(self, key, value):
        if(self.items==self.max_size):
            return False
        index = hash(key) % self.num_buckets
        if(not self.array[index]):
            self.array[index] = Node(key, value, None)
        else:
            self.array[index].setLast(Node(key, value, None))
        self.items += 1
        return True
    
    def get(self, key):
        temp = self.array[hash(key)%self.num_buckets]
        if(not temp):
            return None
        for node in self.array[hash(key)%self.num_buckets].iterateAll():
            if key==node.key:
                return node.value
        return None
    
    def delete(self, key):
        temp = self.array[hash(key)%self.num_buckets]
        if(not temp):
            return None
        if(key==temp.key):
            self.array[hash(key)%self.num_buckets] = temp.next
            return temp.value
        last = temp
        if(not last.next):
            return None
        for each in temp.next.iterateAll():
            if(each.key == key):
                last.next = each.next
                return each.value
            if(not last.next):
                return None
            last = each
        return None
    
    def load(self):
        return self.size/float(self.self.num_buckets)

    def __str__(self):
        # Print out of hashmap in string format is not memory
        #   optimized because of lack of libraries.
        #   No buffers and no StringIO means inefficient string building
        out = ""
        for bucket in range(self.num_buckets):
            out += ("%s | %s\n" % (bucket, self.array[bucket]))
        return out

