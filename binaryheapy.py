class BinaryHeap(object):
    def __init__(self):
        self.array = [None]

    def insert(self, item):
        self.array.append(item)
        print "Inserting"
        self.print_heap()
        self.swim(len(self.array)-1)

    def swim(self, k):
        print "Swimming"
        self.print_heap()
        while (k > 1 and self.array[k] > self.array[k/2]):
            self.exchange(k, k/2)
            k = k/2
            self.print_heap()

    def sink(self, k):
        N = len(self.array) - 1
        print "Sinking"
        self.print_heap()
        while 2*k <= N:
            j = 2*k
            if j < N and (self.array[j] < self.array[j+1]):
                j += 1
            if self.array[j] < self.array[k]:
                break
            self.exchange(j, k)
            k = j
        self.print_heap()

    def delm(self):
        item = self.array[1]
        self.exchange(1, len(self.array)-1)
        self.array = self.array[:len(self.array)-1]
        print "Deleting max"
        self.sink(1)
        self.print_heap()
        return item

    def exchange(self, j, k):
        temp = self.array[j]
        self.array[j] = self.array[k]
        self.array[k] = temp

    def print_heap(self, k=1, depth=1):
        if k == 1:
            print "The tree is"
        if k >= len(self.array):
            return
        print depth*"\t", " ->", self.array[k]
        self.print_heap(2*k, depth+1)
        self.print_heap(2*k + 1, depth+1)

if __name__ == "__main__":
    item = BinaryHeap()
    item.insert(2)
    item.insert(3)
    item.insert(5)
    item.insert(9)
    item.insert(1)
    item.insert(4)
    item.insert(6)
    item.insert(11)
    item.insert(31)
    item.insert(10)
    item.insert(89)
    item.delm()
    item.delm()
    item.insert(89)
