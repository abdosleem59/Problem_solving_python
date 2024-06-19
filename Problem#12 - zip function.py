# Write the code of zip function in python
class OurZip:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.cur_idx =0 


    def has_next(self):
        for seq in self.iterables:
            if self.cur_idx>= len(seq):
                return False
        return True
    

    def get_next(self):
        ret = [0] * len(self.iterables)
        for idx, seq in enumerate(self.iterables):
            ret[idx] = seq[self.cur_idx]
        
        self.cur_idx+=1
        return tuple (ret)


if __name__ == "__main__":
    z = OurZip(list(range(10,15)), list(range(100)), 'Mostafa')
    while z.has_next():
        print(z.get_next())
