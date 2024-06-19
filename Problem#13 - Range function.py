# Problem: Write the code of range() function in python

class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        

    def has_next(self):
        if self.step > 0:
            return self.start < self.end
        return self.start > self.end

    def get_next(self):
        ret = self.start
        self.start += self.step
        return ret


rng = MyRange(10, 5, -1)

while rng.has_next():
    print(rng.get_next())

print("##############################")

rng2 = MyRange(5,10,1)

while rng2.has_next():
    print(rng2.get_next())


